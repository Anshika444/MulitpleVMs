from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response = {"message": "Hello from VM1 Service 1", "status":"success"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"VM1 Service 1 Running")

server_address = ('0.0.0.0', 3000)
httpd = HTTPServer(server_address, RequestHandler)
print("VM1 Service 1 running on port 3000...")
httpd.serve_forever()
