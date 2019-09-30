# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler
import psycopg2
from contextlib import closing
from Shapes.Square import Square
from Shapes.SquareDao import SquareDAO


class NeuroHTTPServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(" bla bla bla ", "utf-8"))

    def do_POST(self):
        self.send_response(200)

        coordinates = (250, 0, 500, 250, 250, 500, 0, 250)

        square = Square(140, 44)
        getSquare = square.get_simpleShape().size
        # square.get_simpleShape().show()

        print(getSquare)
        # var = getSquare
        squareDAO = SquareDAO()
        # squareDAO.addPsycopg2(101, getSquare)
        squareDAO.addPostgresql(101, getSquare)

        self.send_header("Content-type", "application/json")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.wfile.write(bytes(" bla bla bla ", "utf-8"))

'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
hostPort = 9920
global count


class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.attribute = kwargs or None


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        count = count + 1
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % count, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        if self.path == '/mm':
            self.f1()
        if self.path == '/cm':
            self.f2()
        if self.path == '/dm':
            self.f3()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        # Десериализация пример
        p = Person('Alice', 20, nationality='swede', salary=2000)
        with open('person', 'w') as f:
            json.dump(p, f, cls=PersonEncoder)
        print(Person(**json.load(open('person'))))
        self.wfile.write(bytes("<p>You accessed body: %s</p>" % json.dumps(p, cls=PersonEncoder), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def f1(self):
        a = 2
        p = Person('Alice1', 20, nationality='swede', salary=2000)
        with open('person', 'w') as f:
            json.dump(p, f, cls=PersonEncoder)

    def f2(self):
        a = 2
        p = Person('Alice2', 30, nationality='swede', salary=2000)
        with open('person', 'w') as f:
            json.dump(p, f, cls=PersonEncoder)

    def f3(self):
        a = 2
        p = Person('Alice3', 40, nationality='swede', salary=2000)
        with open('person', 'w') as f:
            json.dump(p, f, cls=PersonEncoder)
        self.wfile.write(bytes("</body></html>", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

'''