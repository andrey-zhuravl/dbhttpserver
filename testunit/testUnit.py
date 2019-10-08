import unittest
# from http.server import BaseHTTPRequestHandler, HTTPServer
from fixtures import fixtures as fx
from mycontroller import MyController
import requests
from dao import DAO


class myTestHTTPServer(unittest.TestCase):
    def test_HTTPServerCODE200(self):
        (myURL, myData, codeSuccessful) = fx.fixturePostStatusCode(9)
        req = requests.post(myURL, myData)
        # responseFromHTTP = MyController
        print(req.status_code)
        self.assertEqual(req.status_code, codeSuccessful)

    # def test_HTTPServerURL(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostURL(9)
    #     req = requests.post(myURL, myData)
    #     print(req.url)
    #     nameID = DAO()
    #     self.assertEqual(req.url, myURL)
    #     self.assertEqual(req.url, nameID.insertData(req.url[3]))
    #
    # def test_requestsToHTTPServerCODE200(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID(9)
    #     req = requests.post(myURL, myData)
    #     self.assertEqual(req.status_code, codeSuccessful)
    #
    # def test_requestsToHTTPServerCODE200(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID(9)
    #     req = requests.post(myURL, myData)
    #     self.assertEqual(req.status_code, codeSuccessful)
    #
    # def test_reuestsToHTTPServerJSON(self):
    #     (myURL, myData, myHeader, codeSuccessful) = fx.fixturePostUserID(9)
    #     req = requests.post(myURL, myData)
    #     self.assertEqual(req.status_code, codeSuccessful)
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
