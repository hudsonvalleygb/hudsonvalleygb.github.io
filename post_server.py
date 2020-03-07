from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs

class MessageHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode()
        message = parse_qs(data)
        #self.send_response(301)
        #self.send_header('Location', message['redirect_to'][0])
        self.send_response(200)
        self.send_header('Access-control-allow-origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf8')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
