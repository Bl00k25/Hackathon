from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json


class CallbackHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the incoming request data
        content_length = int(self.headers.get('Content-Length'))
        request_body = self.rfile.read(content_length).decode('utf-8')

        # Log the incoming request data
        print(f"Incoming request data: {request_body}")

        # Send a response back to Airtel Money
        response_data = {"status": "OK"}
        response_body = json.dumps(response_data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', len(response_body))
        self.end_headers()
        self.wfile.write(response_body)


# Create the HTTP server
server_address = ('127.0.0.1', 8080)  # Replace with your desired server address and port
httpd = HTTPServer(server_address, CallbackHandler)

# Start the server
print(f"Server listening on {server_address}")
httpd.serve_forever()
