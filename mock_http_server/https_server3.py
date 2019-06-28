from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus
import ssl
# given a pem file ... openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes

httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,
        certfile='yourpemfile.pem')
httpd.serve_forever()
