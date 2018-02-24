#!/usr/bin/env python 

import os, time
from glob import glob
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from inotify import Inotify
from inotify import EventMask

def StartStream(filename='evf.jpg'):
    boundary = '--msgboundary'
    def request_headers():
        return {
            'Cache-Control': 'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0',
            'Connection': 'close',
            'Content-Type': 'multipart/x-mixed-replace;boundary=%s' % boundary,
            'Expires': 'Mon, 8 Jan 2015 19:40:00 CET',
            'Pragma': 'no-cache',
        }
    def image_headers(filename):
        return {
            'X-Timestamp': time.time(),
            'Content-Length': os.path.getsize(filename),
            'Content-Type': 'image/jpeg',
        }
    def getContents(filename):
        with open(filename, "rb") as f:
            bsize=1024
            byte = f.read(bsize)
            while byte:
                yield byte
                # Next byte
                byte = f.read(bsize)

    def waitForFile():
        global inot
        wd = inot.add_watch('/tmp/aguide/guider2', False)
        for event in inot.getEvents():
            if event:
                (fullpath, masklist) = event
                if 'IN_CLOSE_WRITE' in masklist and fullpath.endswith('.jpg'):
                    inot.rm_wd(wd)
                    return fullpath

    class MjpegFactory(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            # Response headers (multipart)
            for k, v in request_headers().items():
                self.send_header(k, v) 
            # Multipart content
            while True:
                # Part boundary string
                self.end_headers()
                self.wfile.write(boundary)
                self.end_headers()
                #print "wait"
                path = waitForFile()
                print "got: ", path
                # Part headers
                for k, v in image_headers(path).items():
                    self.send_header(k, v)
                self.end_headers()
                # Part binary
                for chunk in getContents(path):
                    self.wfile.write(chunk)
                prev_image = path

        def log_message(self, format, *args):
            pass

    httpd = HTTPServer(('', 5000), MjpegFactory)
    httpd.serve_forever()

inot = Inotify()
#inot.add_watch('/tmp/aguide/guider2', False)

StartStream()
