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
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

    class extendedHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args):
            SimpleHTTPRequestHandler.__init__(self, *args)

        def do_GET(self):
            from urlparse import urlparse,parse_qs
            values = parse_qs(urlparse(self.path).query)
            print type(values), values
            
            SimpleHTTPRequestHandler.do_GET(self)
        def do_POST(self):
            import cgi
            print "handle posting"
            postvars = None
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                postvars = cgi.parse_multipart(self.rfile, pdict)
                print 'multi', postvars
            elif ctype == 'application/x-www-form-urlencoded':
                length = int(self.headers.getheader('content-length'))
                postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
            #self.do_GET()
            return 

    global server
    server = HTTPServer(('', 8000), extendedHandler)
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

