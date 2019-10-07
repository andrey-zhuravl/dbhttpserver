# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from dao import DAO
import json
from io import BytesIO

hostName = "localhost"
hostPort = 9920

class MyController:
    def __init__(self):
        pass
        self.dataAccess = DAO()

    def userInsert(self, userID):
        self.dataAccess.insertData(userID)

    def userUpdate(self, userID):
        self.dataAccess.updateData(userID)

    def userSelect(self, userID):
        self.dataAccess.selectData(userID)

    def userDelete(self, userID):
        self.dataAccess.deleteData(userID)


    def selectNameTable(self, path):
        requestToDB = path.split("/")

        if requestToDB[1] == "users":
            userID = requestToDB[3]
            if requestToDB[2] == "insert":
                self.userInsert(userID)
            elif requestToDB[2] == "update":
                self.userUpdate(userID)
            elif requestToDB[2] == "select":
                self.userSelect(userID)
            elif requestToDB[2] == "delete":
                self.userDelete(userID)

        if requestToDB[1] == "product":
            if requestToDB[2] == "insert":

            elif requestToDB[2] == "update":

            elif requestToDB[2] == "select":

            elif requestToDB[2] == "delete":

        if requestToDB[1] == "order":
            if requestToDB[2] == "insert":

;
            elif requestToDB[2] == "update":

;
            elif requestToDB[2] == "select":
            elif requestToDB[2] == "delete":

    def openDB(self):
        pass

    def dropCollumn(self):
        pass

    def dropTable(self):
        pass

    def addCollumn(self):
        pass


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        path = self.path

        myController = MyController()
        myController.selectNameTable(path, None)
        print("из метода get path = ", path)

        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        cont_len = int(self.headers["Content-Length"])
        body = self.rfile.read(cont_len)
        path = self.path

        myController = MyController()
        myController.requestToDB(path, body)
        self.wfile.write(bytes(path, "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


