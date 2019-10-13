# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from mycontroller import MyController

hostName = "localhost"
hostPort = 9920


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(str(self.path), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("application/json", "text/json")
        self.end_headers()

        cont_len = int(self.headers["Content-Length"])
        body = self.rfile.read(cont_len)
        myController = MyController()
        myController.requestsToDB(self.path, body)

        self.wfile.write(bytes(str(self.path), "utf-8"))
        self.wfile.write(bytes("?", "utf-8"))
        self.wfile.write(body)



myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
