#!/usr/bin/env python

import threading
import time
import signal
import sys
import shutil
import socket

from infolog import InfoLog

#redirect
sys.stderr = sys.stdout

Running = True
def shutdown(signal, frame):
    print "Shutting down..."
    global Running
    Running = False;
    server.shutdown()

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

#globals
capture=False
captureLocation = None
OWN_PORT=8000


lock = threading.RLock()
spotx = -1
spoty = -1
Running = True
server = None
threshold = 15
shutterspeed = 700000
infolog = InfoLog()

class controlFSM:
    def __init__(self):
        self.fsm = [
            #status        #buttontext  #enable threshold control
            ('waitforcam', 'refresh', True),
            ('notrunning', 'LOCK', True),
            ('locked', 'START tracking', False),
            ('tracking', 'STOP tracking', False),
        ]
        self.index = 0

    def shiftFromState(self, prevstate):
        global infolog
        index = 0
        for idx,(s,btn,enableTH) in enumerate(self.fsm):
            if s == prevstate:
                index = idx
                break
        if index == (len(self.fsm) - 1):
            self.index = 1
        else:
            self.index = index + 1
        infolog.add("state: %s" % self.fsm[self.index][0])

    def getState(self):
        return self.fsm[self.index]

cfsm = controlFSM()

def imageProcessor():
    print "starting image processing..."
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor
    from framefactory import CapturedFactory
    import stepperdriver


    infile = 'evf.png'
    evffile = 'evf_%02d.jpg'

    global threshold,shutterspeed,cfsm,lock,infolog,capture,captureLocation
    try:
        if not captureLocation:
            print "using camera as image source"
            cam = FrameFactory()
            Stepper = stepperdriver.NativeStepperDriver
        else:
            print "using pre-captured image sequence"
            cam = CapturedFactory(captureLocation)
            Stepper = stepperdriver.DriverConnector
    except Exception as e:
        print "error", str(e)
        infolog.add("Camera not availble, reboot needed")

    cfsm.shiftFromState('waitforcam')
    counter = 0
    jpegcount = 0
    locked = 0

    with Stepper() as stepper:
        while Running:
            cam.capture(infile)
            if capture:
                #saving input
                shutil.copyfile(infile, '/tmp/cap_%04d.png' % counter) 
                counter += 1
            proc = FrameProcessor(infile, evffile % (jpegcount % 10), threshold)
            jpegcount += 1

            #config settings
            proc.setThreshold(threshold)
            ss = cam.setShutterSpeed(shutterspeed)
            if ss: infolog.add("shutter speed set to: %d\n" % ss)

            if cfsm.getState()[0] == 'locked' or cfsm.getState()[0] == 'tracking':
                locked = 1
            else:
                locked = 0
            global spotx,spoty
            x,y = proc.getSpotCoordinates(locked, spotx, spoty)
            if x == -1 and y == -1 and locked:
                locked = 0
                infolog.add("spot is lost, unlocked.")
                cfsm.shiftFromState('tracking')
                continue
            with lock:
                if spotx != x or spoty !=y and cfsm.getState()[0] == 'tracking':
                    #moved away...
                    diffx = x - spotx
                    diffy = y - spoty
                    infolog.add('move offset: [%d:%d]' % (diffx, diffy))
                    if diffx > 0:
                        #actual movement
                        stepper.doStep(diffx)
            spotx = x
            spoty = y

def startUI():
    print "starting webservice..."
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from indexpage import IndexPage,ConfigPage

    #init view
    state,buttontext,enableTH = cfsm.getState()
    IndexPage(state, 'loading.png', buttontext)

    global captureLocation

    class extendedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args):
            SimpleHTTPRequestHandler.__init__(self, *args)

        def log_message(self, format, *args):
            pass

        def do_GET(self):
            global cfsm,threshold,shutterspeed,infolog,OWN_PORT
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            path = urlparse(self.path).path
            state,buttontext,enableTH = cfsm.getState()

            if 'shutterspeed' in values:
                shutterspeed = int(values['shutterspeed'][0])
            if 'threshold' in values:
                threshold = int(values['threshold'][0])
            if 'current_state' in values:
                cfsm.shiftFromState(values['current_state'][0])
                state,buttontext,enableTH = cfsm.getState()
                ip_addr = socket.gethostbyname(socket.gethostname())
                IndexPage(state, 'http://' + str(ip_addr) + ':5000', buttontext)

            if path == "/config.html":
                ConfigPage(threshold, shutterspeed)

            #the rest
            SimpleHTTPRequestHandler.do_GET(self)

    global server,OWN_PORT
    server = HTTPServer(('', OWN_PORT), extendedHandler)
    server.serve_forever()

if __name__ == "__main__":            
    print "starting up buksiguider9000"
    if len(sys.argv) >= 2:
        print "entering TEST MODE"
        if sys.argv[1] == '--capture':
            capture=True
            print "Capturing enabled"
            infolog.add("CAPTURING ENABLED")
        if sys.argv[1] == '--replay':
            try:
                captureLocation = sys.argv[2]
            except:
                print "file pattern has to be specified"
                sys.exit(1)
            print "replaying captured shots from: ", captureLocation
            infolog.add("REPLAYING")
    else:
        print "TEST MODE disabled"
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()
    while Running:
        state,buttontext,enableTH = cfsm.getState()
        if state != 'waitforcam':
            pass
        time.sleep(1)

    #exiting
    thread_ui.join()
    thread_ch.join()
