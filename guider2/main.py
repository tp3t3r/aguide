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
spotx = -1
spoty = -1
Running = True
server = None

class controlFSM:
    def __init__(self):
        self.fsm = [
            #status        #buttontext
            ('waitforcam', 'N/A'),
            ('notrunning', 'lock'),
            ('locked', 'start tracking'),
            ('tracking', 'stop tracking'),
        ]
        self.index = 0

    def shiftFromState(self, prevstate):
        index = 0
        for idx,(s,btn) in enumerate(self.fsm):
            if s == prevstate:
                index = idx
                break
        if index == (len(self.fsm) - 1):
            self.index = 1
        else:
            self.index = index + 1

    def getState(self):
        return self.fsm[self.index]

cfsm = controlFSM()

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    global cfsm,lock

    cam = FrameFactory()
    cfsm.shiftFromState('waitforcam')
    while Running:
        #print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile)
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
            global cfsm
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            state,buttontext = cfsm.getState()
            if state == 'waitforcam':
                IndexPage(state, 'loading.png', buttontext)
            if 'current_state' in values:
                cfsm.shiftFromState(values['current_state'][0])
                state,buttontext = cfsm.getState()
                IndexPage(state,'evf.jpg',buttontext)

            #the rest
            SimpleHTTPRequestHandler.do_GET(self)

    global server
    server = HTTPServer(('', 8000), extendedHandler)
    server.serve_forever()

if __name__ == "__main__":            
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()    
    while Running:
        state,buttontext = cfsm.getState()
        if state != 'waitforcam':
            #print 'spot: ', spotx, ":", spoty
            pass
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()

