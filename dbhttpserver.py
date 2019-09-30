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
    def tableUser(self):
        pass

    def tableProduct(self):
        pass

    def tableOrder(self):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = "Server working!"

        self.wfile.write(bytes(message, "utf-8"))

        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        txt = "postgres.public.users"
        x = txt.split("#", 1)

        content_length = int(self.headers['Content-Length'])
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
