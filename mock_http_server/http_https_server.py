# given a pem file ... openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes
import sys
import ssl
import time
import signal
import threading
import BaseHTTPServer, SimpleHTTPServer


def http_worker():
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), SimpleHTTPServer.SimpleHTTPRequestHandler)
    httpd.serve_forever()
    return

def https_worker():
    httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, server_side=True,
            certfile='yourpemfile.pem')
    httpd.serve_forever()
    return

def signal_handler(sig, frame):
        print('You pressed Ctrl+C! Now exiting')
        sys.exit(0)

if __name__ == "__main__":
    # http server
    http = threading.Thread(name='httpserver', target=http_worker)
    http.setDaemon(True)

    # https server
    https = threading.Thread(name='httpsserver',target=https_worker)
    https.setDaemon(True)

    http.start()
    https.start()

    # catch ctrl+c to exit the script
    signal.signal(signal.SIGINT, signal_handler)
    print("Press CTRL+C to stop the script")
    signal.pause()

