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

    def requestsToDB(self, path, body):
        request = path.split("/")
        data = json.dumps(body)
        print("data - body.json() = ", data)
        print("тип данных - body.json() = ", type(data))

        if request[1] == "users":
            userID = request[3]
            if request[2] == "insert":
                self.userInsert(userID)
            elif request[2] == "update":
                self.userUpdate(userID)
            elif request[2] == "select":
                self.userSelect(userID)
            elif request[2] == "delete":
                self.userDelete(userID)

    #
    #     if request[1] == "product":
    #         if request[2] == "insert":
    #
    #         elif request[2] == "update":
    #
    #         elif request[2] == "select":
    #
    #         elif request[2] == "delete":
    #
    #     if request[1] == "order":
    #         if request[2] == "insert":
    #
    #         elif request[2] == "update":
    #
    #         elif request[2] == "select":
    #
    #         elif request[2] == "delete":

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
        myController.requestsToDB(path, None)
        print("из метода get path = ", path)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        cont_len = int(self.headers["Content-Length"])
        bodyBytes = self.rfile.read(cont_len)
        bodyJson = json.loads(bodyBytes)
        print("boduJson = ", bodyJson)
        path = self.path

        myController = MyController()
        myController.requestsToDB(path, bodyJson)
        self.wfile.write(bytes(path, "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
