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

status = {
    'camready' : False,
    'islocked' : False,
    'running' : False,
}

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    global status,lock

    cam = FrameFactory()
    status['camready'] = True
    while Running:
        #print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile)
        proc.lockSpot(status['islocked'])

        x,y = proc.getSpotCoordinates()
        with lock:
            spotx = x
            spoty = y

def processButtons(values):
    global status,lock
    if 'lock' in values:
        with lock:
            status['islocked'] = not status['islocked']
    if 'start/stop' in values:
        with lock:
            status['running'] = not status['running']
    print status

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
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            #print "path: ", self.path
            #print type(values), values
            processButtons(values)

            #template tricks
            state = 'not running'
            evf = 'loading.png'
            if status['running']:
                state = 'running'
            if status['camready']:
                evf = 'evf.jpg'
            
            IndexPage(state, evf)
            try:
                SimpleHTTPRequestHandler.do_GET(self)
            except socket.error:
                print "terrible thing"
    global server
    server = HTTPServer(('', 8000), extendedHandler)
    server.serve_forever()

if __name__ == "__main__":            
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()    
    while Running:
        if status['running']:
            print 'spot: ', spotx, ":", spoty
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()

