# Multiple types of HTTP(s) servers in python 2 and python 3
Depending on the need, see following POC scripts. Note the scripts are running localhost and on high ports for user execution.
Scripts run on port 8080 or port 4443

# Mock HTTP Server with POST printing
A mock HTTP server found in a Gist that starts a basic HTTP server for testing purposes. 
The HTTP server Responds to the following methods:
- GET
- POST
- HEAD

For POST requests, the data submitted is printed in stdout.

## Example queries
### Start the script
```python http_server.py <port>```

### GET
```curl http://localhost```

### POST
```curl -d "foo=bar&bin=baz" http://localhost```

### HEAD
```curl -I http://localhost```

# Mock HTTPS Server
- https_server.py == python 2.7
- https_server3.py == python3.x 

A certificate can be generated with the following command (also in a comment in the scripts)
``` openssl req -new -x509 -keyout yourpemfile.pem -out yourpemfile.pem -days 365 -nodes ```

