from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # Begin the response
        self.send_response(200)
        self.end_headers()
        self.wfile.write('client: %s\n' % str(self.client_address))
        self.wfile.write('user-agent: %s\n' % str(self.headers['user-agent']))
        self.wfile.write('path: %s\n' % self.path)

        self.wfile.write('form data:\n')
        # Echo back information about what was posted in the form
        for field in form.keys():
            self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return
