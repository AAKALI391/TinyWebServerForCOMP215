from http.server import HTTPServer, BaseHTTPRequestHandler

host = "192.168.5.143"
port = 8000

class HandleRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        in_file = open("web_server_test\content.htm", "rb")
        self.wfile.write(in_file.read())
        in_file.close()
    
  
        
server = HTTPServer((host,port),HandleRequests)
print("Server running at IP adress, ", host," on port ",port)
server.serve_forever()
server.server_close()