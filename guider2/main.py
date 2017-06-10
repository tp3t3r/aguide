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

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    cam = FrameFactory()
    while Running:
        #print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile)
        x,y = proc.getSpotCoordinates()
        with lock:
            spotx = x
            spoty = y
        

def startUI():
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    '''
    class CustomHTTPServer(HTTPServer):
        def __init__(self, *args, **kwargs):
            super(type(self),self).__init__(*args, **kwargs)

        def serve_forever(self):
            while Running:
                self.handle_request()
    '''
    global server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":            
    thread_ui = threading.Thread(target=startUI)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()

    while Running:
        print "main thread"
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()

