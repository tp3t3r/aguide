import os, time
from glob import glob
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

boundary = '--boundarydonotcross'

def request_headers():
    return {
        'Cache-Control': 'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0',
        'Connection': 'close',
        'Content-Type': 'multipart/x-mixed-replace;boundary=%s' % boundary,
        'Expires': 'Mon, 3 Jan 2000 12:34:56 GMT',
        'Pragma': 'no-cache',
    }

def image_headers(filename):
    return {
        'X-Timestamp': time.time(),
        'Content-Length': os.path.getsize(filename),
        #FIXME: mime-type must be set according file content
        'Content-Type': 'image/jpeg',
    }

# FIXME: should take a binary stream
def image(filename):
    with open(filename, "rb") as f:
        # for byte in f.read(1) while/if byte ?
        byte = f.read(1)
        while byte:
            yield byte
            # Next byte
            byte = f.read(1)

# Basic HTTP server
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # Response headers (multipart)
        for k, v in request_headers().items():
            self.send_header(k, v) 
        # Multipart content
        for filename in glob('img/*'):
            # Part boundary string
            self.end_headers()
            self.wfile.write(boundary)
            self.end_headers()
            # Part headers
            for k, v in image_headers(filename).items():
                self.send_header(k, v)
            self.end_headers()
            # Part binary
            for chunk in image(filename):
                self.wfile.write(chunk)
            time.sleep(0.04)
    def log_message(self, format, *args):
        return

httpd = HTTPServer(('', 8080), MyHandler)
httpd.serve_forever()
