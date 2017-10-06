from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import json

hostName = "localhost"
hostPort = 9000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("path is %s" % self.path)
        if self.path is "/":
            print("index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = open("status.html", "rb")
            self.wfile.write(html.read())
            html.close()

        elif self.path == "/nico.jpg":
            print("niconicoicon")
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            nico = open("nico.jpg", "rb")
            self.wfile.write(nico.read())
            nico.close()

        elif self.path == "/config":
            print("accessed config")
            self.send_response(200)
            self.send_header("Content-type", "text/x-yaml")
            self.end_headers()
            config = open("config.yaml", "rb")
            self.wfile.write(config.read())
            config.close()

        elif self.path == "/sounds.json":
            print("accessed sounds?")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"c": 0, "b": 0, "a": 0}
            s = json.dumps(data, sort_keys=True)
            self.wfile.write(bytes(s, "utf-8"))

        elif self.path == "/users.json":
            print("accessed users")
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = ['tom@gmail.com', 'sally@gmail.com']
            s = json.dumps(data, sort_keys=True)
            self.wfile.write(bytes(s, "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyHandler)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))