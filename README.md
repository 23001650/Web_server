# Developing a Simple Webserver
Name: SUNIL KUMAR T

Ref no:23001650
# AIM:

Develop a webserver to display about top five web application development frameworks.

# DESIGN STEPS:

## Step 1:

HTML content creation is done

## Step 2:

Design of webserver workflow

## Step 3:

Implementation using Python code

## Step 4:

Serving the HTML pages.

## Step 5:

Testing the webserver
# PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<?head>
<body>
<h1>Wlcome</h1>
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

```
# OUTPUT:
![output](/Web_server/webserver.jpg)

# RESULT:

The program is executed succesfully
