import unittest
# from http.server import BaseHTTPRequestHandler, HTTPServer
from fixtures import fixtures as fx
from dbhttpserver.dbhttpserver import *
import requests

class myTestHTTPRequests(unittest.TestCase):
    #
    # def test_reuestsToHTTPServerURL(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID()
    #     # my = MyServer()
    #     req = requests.post(myURL, myData)
    #     print(myURL)
    #     self.assertEqual(req.url, myURL)

    def test_reuestsToHTTPServerCODE200(self):
        (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID()
        myServer = MyServer()
        req = requests.post(myURL, myData)

        print(req.status_code)
        print(codeSuccessful)
        print(myServer.do_POST())

        self.assertEqual(req.status_code, codeSuccessful)
    #
    # def test_reuestsToHTTPServerJSON(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID()
    #     myServer = MyServer()
    #     print(myServer.do_POST())
    #     req = requests.post(myURL, myData)
    #     self.assertEqual(req.json, myData)

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
