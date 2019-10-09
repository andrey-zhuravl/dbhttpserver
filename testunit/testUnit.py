import unittest
# from http.server import BaseHTTPRequestHandler, HTTPServer
from fixtures import fixtures as fx
from mycontroller import MyController
import requests
import json
from dao import DAO


class myTestHTTPServer(unittest.TestCase):

    def test_HTTPServerCODE200(self):
        (myURL, myData, codeSuccessful) = fx.fixturePostStatusCode(9)
        req = requests.post(myURL, params=myData)
        print(req.status_code)
        print("  THIS IS TEST code 200 = ", req.status_code)
        responseFromHTTP = MyController()
        responseFromHTTP.requestsToDB(req.url, myData)
        self.assertEqual(req.status_code, codeSuccessful)

    def test_HTTPServerURL(self):
        (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostURL(9)
        req = requests.post(myURL, myData)
        print("  THIS IS TEST URL - REQ.URL = ", req.url)
        # responseFromHTTP = MyController()
        # responseFromHTTP.requestsToDB(req.url.split("/"))
        self.assertEqual(req.url, myURL)

    def test_HTTPServerJSON(self):
        (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostURL(9)
        req = requests.post(myURL, myData)
        print("  THIS IS TEST json - REQ.JSON = ", req.json())
        self.assertEqual(req.json(), myData)

    # r.status_code
    # r.json()

    # url = "http://localhost:8080"
    # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)

    # 1. путь
    # 2. тело в формате json
    # 3. заголовки)


if __name__ == '__main__':
    unittest.main()
