#!/usr/bin/env python

import threading
import time
import signal
import sys

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
OWN_IP='192.168.0.1'
OWN_PORT=8000


lock = threading.RLock()
spotx = 1
spoty = -1
Running = True
server = None
threshold = 170
shutterspeed = 600000
infolog = ""

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
        infolog += "new state: %s\n" % self.fsm[self.index][0]

    def getState(self):
        return self.fsm[self.index]

cfsm = controlFSM()

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    global threshold,shutterspeed,cfsm,lock,infolog
    try:
        cam = FrameFactory()
    except Exception as e:
        infolog += "Camera not availble, reboot needed\n%s\n" % str(e)

    cfsm.shiftFromState('waitforcam')
    while Running:
        #print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile, threshold)

        #config setttngs
        proc.setThreshold(threshold)
        cam.setShutterSpeed(shutterspeed)

        if cfsm.getState()[0] == 'locked':
            proc.lockSpot(True)
        else:
            proc.lockSpot(False)

        x,y = proc.getSpotCoordinates()
        with lock:
            spotx = x
            spoty = y

def startUI():
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from indexpage import IndexPage

    #init view
    state,buttontext,enableTH = cfsm.getState()
    IndexPage(state, 'loading.png', infolog, buttontext)

    class extendedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args):
            SimpleHTTPRequestHandler.__init__(self, *args)

        def log_message(self, format, *args):
            pass

        def do_GET(self):
            global cfsm,threshold,shutterspeed,infolog,OWN_IP,OWN_PORT
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            state,buttontext,enableTH = cfsm.getState()

            if urlparse(self.path).path == "/config.html":
                #setup
                values = parse_qs(urlparse(self.path).query)
                if 'shutterspeed' in values:
                    shutterspeed = int(values['shutterspeed'][0])
                if 'threshold' in values:
                    threshold = int(values['threshold'][0])
                #return to main page 
                print values, type(values)
                #if values:
                #    self.send_response(301)
                #    self.send_header('Location', 'http://%s:%d/index.html' % (OWN_IP, OWN_PORT))
                #    self.end_headers()
            else:
                #main GUI
                #handles state transitions
                if 'current_state' in values:
                    cfsm.shiftFromState(values['current_state'][0])
                    state,buttontext,enableTH = cfsm.getState()
                    IndexPage(state, 'evf.jpg', infolog, buttontext)

            #the rest
            SimpleHTTPRequestHandler.do_GET(self)

    global server,OWN_PORT
    server = HTTPServer(('', OWN_PORT), extendedHandler)
    server.serve_forever()

if __name__ == "__main__":            
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()
    while Running:
        state,buttontext,enableTH = cfsm.getState()
        if state != 'waitforcam':
            infolog += "spot[%d:%d]\n" % (spotx,spoty)
        time.sleep(2)
        print infolog

    #exiting
    thread_ui.join()
    thread_ch.join()

