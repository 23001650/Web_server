from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<?head>
<body>
<h1>SUNIL KUMAR T</h1>
<h1>Artifical intelligence and machine learning</h1>
</body>
</html>
"""

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())
        
  
  
server_address = ('', 80)
httpd = HTTPServer(server_address,HelloHandler)
httpd.serve_forever()      

