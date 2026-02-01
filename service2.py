from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import json

VM1_IP = "192.168.157.4"  # Replace if different
VM1_PORT = 3000

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                url = f"http://{VM1_IP}:{VM1_PORT}/data"
                with urllib.request.urlopen(url) as response:
                    data = response.read()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"VM2 got from VM1: " + data)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error: {e}".encode())

server_address = ('0.0.0.0', 4000)
httpd = HTTPServer(server_address, RequestHandler)
print("VM2 Service 2 running on port 4000...")
httpd.serve_forever()
