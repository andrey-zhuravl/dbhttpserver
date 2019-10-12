# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from mycontroller import MyController

hostName = "localhost"
hostPort = 9920

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        path = self.path

        # myController = MyController()
        # myController.requestsToDB(path, None)
        # print("из метода get path = ", path)

    def do_POST(self):
        self.send_response(200)
        self.send_header("application/json", "text/json")
        self.end_headers()

        cont_len = int(self.headers["Content-Length"])
        bodyBytes = self.rfile.read(cont_len)
        print("bodyBytes = ", bodyBytes)

        bodyJson = json.loads(bodyBytes)
        print("bodyJson = ", bodyJson)

        print("send_response = ", self.send_response(200))
        print("client_address = ", self.client_address)
        print("server = ", self.server)
        print("command = ", self.command)
        print("headers = ", self.headers)

        print("path = ", self.path)
        print("server_version = ", self.server_version)
        print("address_string() = ", self.address_string())
        print("\n")

        myController = MyController()
        # myController.requestsToDB(self.path, bodyJson)
        myController.requestsToDB(self.path, bodyBytes)

        # req.content   =  b'   ....
        # req.text      =       ....

        self.wfile.write(bodyBytes)
        self.wfile.write(bytes("?", "utf-8"))
        self.wfile.write(bytes(str(self.path), "utf-8"))

        # self.wfile.write(self.path)

        # self.wfile.write(bodyBytes)


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
