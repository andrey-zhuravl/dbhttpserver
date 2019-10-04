# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from io import BytesIO

hostName = "localhost"
hostPort = 9920


class MyController:
    def __init__(self):
        pass

    def tableUsers(self, nameTable):
        nameCollumn = nameTable[0]
        newNameUser = nameTable[1]
        print("nameCollumn = ", nameCollumn)
        print("newNameUser = ", newNameUser)

    def tableProduct(self, nameTable):
        nameCollumn = nameTable[0]
        newProduct = nameTable[1]
        print("nameCollumn = ", nameCollumn)
        print("newNameUser = ", newProduct)

    def tableOrder(self, nameTable):
        nameCollumn = nameTable[0]
        newOrder = nameTable[1]
        print("nameCollumn = ", nameCollumn)
        print("newNameUser = ", newOrder)

    def selectNameTable(self, body):
        nameTable = body.split("/")
        print("nameTable = ", nameTable)

        if nameTable[0] == "users":
            self.tableUsers(nameTable[1:])
        elif nameTable[0] == "product":
            self.tableProduct(nameTable[1:])
        elif nameTable[0] == "order":
            self.tableOrder(nameTable[1:])


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        cont_len = int(self.headers["Content-Length"])

        body = self.rfile.read(cont_len)
        path = self.path
        print("path = ", path)
        print("body = ", body)

        # nameTable = MyController()
        # nameTable.selectNameTable(body)

        self.wfile.write(bytes("message", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
