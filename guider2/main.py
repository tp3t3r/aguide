#!/usr/bin/env python

import threading
import time
import signal
import sys
import shutil

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
capturedPattern = None
OWN_IP='192.168.0.1'
OWN_PORT=8000


lock = threading.RLock()
spotx = 1
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
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor
    from framefactory import CapturedFactory

    infile = 'evf.png'
    evffile = 'evf_%02d.jpg'

    global threshold,shutterspeed,cfsm,lock,infolog,capture,capturedPattern
    try:
        if not capturedPattern:
            cam = FrameFactory()
        else:
            cam = CapturedFactory(capturedPattern)
    except Exception as e:
        print "error", str(e)
        infolog.add("Camera not availble, reboot needed")

    cfsm.shiftFromState('waitforcam')
    counter = 0
    jpegcount = 0
    while Running:
        #print "capturing @", time.time()
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
        if ss: print "shutter speed set to: %d\n" % ss
        if cfsm.getState()[0] == 'locked' or cfsm.getState()[0] == 'running':
            proc.lockSpot(True)
        else:
            proc.lockSpot(False)
        x,y = proc.getSpotCoordinates()
        with lock:
            global spotx, spoty
            if spotx != x or spoty !=y:
                #moved away...
                if cfsm.getState()[0] == 'locked' or cfsm.getState()[0] == 'running':
                    infolog.add('delta: [%d:%d]' % (x-spotx, y-spoty))
            spotx = x
            spoty = y

def startUI():
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from indexpage import IndexPage,ConfigPage

    #init view
    state,buttontext,enableTH = cfsm.getState()
    IndexPage(state, 'loading.png', buttontext)

    class extendedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args):
            SimpleHTTPRequestHandler.__init__(self, *args)

        def log_message(self, format, *args):
            pass

        def do_GET(self):
            global cfsm,threshold,shutterspeed,infolog,OWN_IP,OWN_PORT
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
                IndexPage(state, 'http://192.168.0.1:5000', buttontext)

            if path == "/config.html":
                ConfigPage(threshold, shutterspeed)

            #the rest
            SimpleHTTPRequestHandler.do_GET(self)

    global server,OWN_PORT
    server = HTTPServer(('', OWN_PORT), extendedHandler)
    server.serve_forever()

if __name__ == "__main__":            
    if len(sys.argv) == 2:
        if sys.argv[1] == '--capture':
            capture=True
            print "Capturing enabled"
            infolog.add("CAPTURING ENABLED")
        if sys.argv[1] == '--replay':
            capturedPattern = '/home/peter/capture/cap*.png'
            print "replaying captured shots"
            infolog.add("REPLAYING")
                
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()
    while Running:
        state,buttontext,enableTH = cfsm.getState()
        if state != 'waitforcam':
            pass
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()


