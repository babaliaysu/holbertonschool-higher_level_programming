#!/usr/bin/env python3
"""Sadə HTTP API server modulu."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """HTTP muracietlerini idare eden klas."""

    def do_GET(self):
        """GET muracietlerini qebul edir ve endpoint-e gore cavab verir."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(port=8000):
    """Serveri mueyyen olunmus portda ise salir."""
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server http://localhost:{port} unvaninda isleyir...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
