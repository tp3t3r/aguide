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
lock = threading.RLock()
spotx = 1
spoty = -1
Running = True
server = None

threshold = 170
infolog = ""

class controlFSM:
    def __init__(self):
        self.fsm = [
            #status        #buttontext  #enable threshold control
            ('waitforcam', 'N/A', True),
            ('notrunning', 'lock', True),
            ('locked', 'start tracking', False),
            ('tracking', 'stop tracking', False),
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
        infolog += "new state: %s\n" % self.fsm[self.index]

    def getState(self):
        return self.fsm[self.index]

cfsm = controlFSM()

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    global threshold,cfsm,lock,infolog
    try:
        cam = FrameFactory()
    except Exception as e:
        infolog += "Camera not availble, reboot needed\n%s\n" % str(e)

    cfsm.shiftFromState('waitforcam')
    while Running:
        #print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile)
        if proc.setThreshold(threshold):
            print "threshold is set to: %d\n" % threshold
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

    class extendedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args):
            SimpleHTTPRequestHandler.__init__(self, *args)

        def log_message(self, format, *args):
            pass

        def do_GET(self):
            global cfsm,threshold,infolog
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            state,buttontext,enableTH = cfsm.getState()
            if state == 'waitforcam':
                IndexPage(state, 'loading.png', infolog, buttontext,threshold)

            #handle threshold setting
            if 'threshold' in values and enableTH:
                print values
                with lock:
                    if int(values['threshold'][0]) != threshold:
                        threshold = int(values['threshold'][0])

            #handles state transitions
            if 'current_state' in values:
                cfsm.shiftFromState(values['current_state'][0])
                state,buttontext,enableTH = cfsm.getState()
                IndexPage(state, 'evf.jpg', infolog, buttontext, threshold)

            #the rest
            SimpleHTTPRequestHandler.do_GET(self)

    global server,infolog
    server = HTTPServer(('', 8000), extendedHandler)
    try:
        server.serve_forever()
    except Exception as e:
         infolog += "bad happened: %s\n" % str(e)

if __name__ == "__main__":            
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()    
    while Running:
        state,buttontext,enableTH = cfsm.getState()
        if state != 'waitforcam':
            #print 'spot: ', spotx, ":", spoty
            pass
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()

