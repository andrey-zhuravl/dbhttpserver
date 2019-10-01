# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
hostPort = 8081


class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.attribute = kwargs or None


class MyServer(BaseHTTPRequestHandler):

    def tableUser(self, nameTable, postBody):
        pass

    def tableProduct(self, nameTable, postBody):
        pass

    def tableOrder(self, nameTable, postBody):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # ввел этот блок для проверки через браузер, или Insomnia
        path = "users/user_name"
        nameTable = path.split("/", maxsplit=1)
        self.wfile.write(bytes(nameTable[0]*9, "utf-8"))

        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        postBody = 15
        path = "users/user_name"
        nameTable = path.split("/", maxsplit=1)

        if nameTable[0] == "users":
            self.tableUser(nameTable[1], postBody)
        elif nameTable[0] == "product":
            self.tableProduct(nameTable[1], postBody)
        elif nameTable[0] == "order":
            self.tableOrder(nameTable[1], postBody)

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        self.wfile.write(bytes("message", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
