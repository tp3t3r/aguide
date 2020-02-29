#!/usr/bin/env python
import argparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def log_message(self, *args):
        pass

    def mainPage(self):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = """
        <html>
        <body>
        <p>form:</p>
        <form action="input.form" method="post">
        <label for="value1">Value1</label>
        <input type="text" id="value1" name="nvalue1"><br>
        <label for="value2">Value2</label>
        <input type="text" id="value2" name="nvalue2"><br>
        <input type="submit" value="Send">
        </form>
        </body>
        </html>
        """
        return content.encode("utf8")  # NOTE: must return a bytes object!

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
