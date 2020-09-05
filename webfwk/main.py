#!/usr/bin/env python
import argparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time, os
import mimetypes

class GuiderFSM():
    def __init__(self):
        self.states = [ "WAIT-FOR-CAM", "FREE-RUN", "LOCKED", "TRACKING" ]
        self.currstate = self.states[0]
        self.reqcount = 0

    def getReqCount(self): # for mocking purposes
        return self.reqcount

    def getState(self):
        self.reqcount = self.reqcount + 1
        return self.currstate

    def setState(self, state):
        print("---set: ",state)
        if state in self.states:
            self.currstate = state
        else:
            pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self

class ReqHandler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def mainPage(self):
        with open("templates/main.html.template", "r") as main:
            return main.read().format().encode("utf8")

    def __serveFile(self, filename):
        try:
            with open(filename, "r") as f:
                self.wfile.write(f.read())
        except:
            self.wfile.write(self.mainPage())
            pass

    def do_GET(self):

        # check FSM changes
        print("++++", fsm.getReqCount())
        if fsm.getReqCount() == 5:
            fsm.setState("FREE-RUN")

        self.path = self.path.split("?")[0]
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.mainPage())
            return
         # status
        if self.path == "/state":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(fsm.getState().encode("utf8"))
            return
        # file contents
        self.path = "." + self.path
        if os.path.isfile(self.path):
           ctype = mimetypes.guess_type(self.path)[0]
           self.send_response(200)
           self.send_header("Content-type", ctype)
           self.end_headers()
           self.__serveFile(self.path)
           return
       # 404
        else:
            self.send_response(404)
            self.end_headers()
            return

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print self.headers, length
        print self.rfile.read(length)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.wfile.write(self.mainPage())


if __name__ == "__main__":
    with GuiderFSM() as fsm:
        httpd = HTTPServer(("0.0.0.0", 8000), ReqHandler)
        httpd.serve_forever()
