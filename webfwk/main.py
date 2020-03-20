#!/usr/bin/env python
import argparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time, os
import mimetypes

from content import skeleton


class ReqHandler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def mainPage(self):
        return skeleton.encode("utf8")  # NOTE: must return a bytes object!

    def __serveFile(self, filename):
        try:
            with open("." + filename, "r") as f:
                self.wfile.write(f.read())
        except:
            # TODO handle index page 
            self.wfile.write(self.mainPage())
            pass

    def do_GET(self):
        if self.__sendHeaders(self.path):
            self.__serveFile(self.path)

    def __sendHeaders(self, path):
        if path == "/": # the index page
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            return True
        if os.path.isfile("." + path):
            ctype = mimetypes.guess_type("." + path)[0]
            print ctype
            self.send_response(200)
            self.send_header("Content-type", ctype)
            self.end_headers()
            return True
        else:
            self.send_response(404)
            self.end_headers()
            return False

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print self.headers, length
        print self.rfile.read(length)
        #elf.__sendHeaders()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.wfile.write(self.mainPage())


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8000), ReqHandler)
    httpd.serve_forever()
