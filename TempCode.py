from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 8080

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Python server\n")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        print("Received POST body:", body.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST received\n")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SimpleHandler)
    print(f"Server listening on http://{HOST}:{PORT}")
    server.serve_forever()
