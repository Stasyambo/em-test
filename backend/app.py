from http.server import SimpleHTTPRequestHandler, HTTPServer

class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

HTTPServer(("0.0.0.0", 8080), H).serve_forever()
