# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
hostPort = 9920


class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.attribute = kwargs or None


class MyController:
    def __init__(self):
        pass

    def tableUsers(self, nameTable):
        nameCollumn = nameTable[0]
        newNameUser = nameTable[1]

    def tableProduct(self, nameTable):
        nameCollumn = nameTable[0]
        newNameUser = nameTable[1]

    def tableOrder(self, nameTable):
        nameCollumn = nameTable[0]
        newOrder = nameTable[1]

    def selectNameTable(self, body):    # должно быть nameTable[0]
        nameTable = body.split("/")  # предполагается формат body - table/collumn/value
        print("nameTable = ", nameTable)                                # т.е. будет nameTable["table", "collumn", value(int или str)]

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
        body = str(self.rfile.read(cont_len))[2:] # body из Insomnia приходит в виде битовых данных

        nameTable = MyController()
        nameTable.selectNameTable(body)

        self.wfile.write(bytes("message", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

# print("body = ", body)
# print("cont_len_int = ", cont_len_int)
# print("type(cont_len_int) = ", type(cont_len_int))
#
# print("cont_len_str = ", cont_len_str)
# print("type(cont_len_str) = ", type(cont_len_str))
