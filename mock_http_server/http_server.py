import BaseHTTPServer, SimpleHTTPServer
import ssl

# given a pem file ... openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes

httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.serve_forever()
