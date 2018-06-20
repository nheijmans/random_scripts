# Mock HTTP Server
A mock HTTP server found in a Gist that starts up a very simple HTTP server for testing purposes. 
It responds to the following methods:
- GET
- POST
- HEAD

For POST requests, the data submitted is printed.

## Example queries
### Start the script
```python http_server.py <port>```

### GET
```curl http://localhost```

### POST
```curl -d "foo=bar&bin=baz" http://localhost```

### HEAD
```curl -I http://localhost```
