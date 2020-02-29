#!/usr/bin/env python
import argparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from content import skeleton


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def log_message(self, *args):
        pass

    def mainPage(self):
        return skeleton.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        print self.headers
        self._set_headers()
        self.wfile.write(self.mainPage())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print self.headers, length
        print self.rfile.read(length)
        self._set_headers()
        self.wfile.write(self.mainPage())


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8000), S)
    httpd.serve_forever()
