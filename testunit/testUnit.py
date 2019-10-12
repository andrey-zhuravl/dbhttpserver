import unittest
from fixtures import fixtures as fx
from mycontroller import MyController
import requests
import json
from dao import DAO

class myTestHTTPServer(unittest.TestCase):

    def test_HTTPServerPostMyServerCODE200(self):
        (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
        self.assertEqual(req.status_code, codeSuccessful)

    def test_HTTPServerPostMyServerURL(self):
        (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
        self.assertEqual(req.url, myURL+myPath)

    def test_HTTPServerPostMyServerPath(self):
        (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
        path = req.text.split("?")[1]
        self.assertEqual(path, myPath)

    def test_HTTPServerPostMyServerBody(self):
        (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
        body = req.text.split("?")[0]
        self.assertEqual(body, json.dumps(myBody))

#==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==#

    def test_HTTPServerGetMyServerCODE200(self):
        (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
        req = requests.get(myURL+myPath)
        print(" Get200 = ", req.status_code)
        self.assertEqual(req.status_code, codeSuccessful)

    def test_HTTPServerGetMyServerURL(self):
        (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
        req = requests.get(myURL+myPath)
        print(" GetURL = ", req.url)
        self.assertEqual(req.url, myURL+myPath)

    def test_HTTPServerGetMyServerPath(self):
        (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
        req = requests.get(myURL+myPath)
        path = req.text
        print(" GetPath = ", path)
        self.assertEqual(path, myPath)

#==MyController==MyController==MyController==MyController==MyController==MyController==#

    def test_HTTPServerPostMyControllerUserInsert(self):
        (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)

        resp = MyController()
        resp.requestsToDB(req.url.split("/"))
        # остаток пути      /insert/9
        # название функции  /userInsert
        self.assertEqual(req.status_code, codeSuccessful)

#       pass
#
#     def test_HTTPServerPostMyControllerUserUpdate(self):
#         # остаток пути      /update
#         # название функции  /userInsert
#         pass
#
#     def test_HTTPServerPostMyControllerUserSelect(self):
#         # остаток пути      /select
#         # название функции  /userInsert
#         pass
#
#
#     def test_HTTPServerGetMyControllerUserInsert(self):
#         # остаток пути      /insert
#         # название функции  /userInsert
#         pass
#
#     def test_HTTPServerGetMyControllerUserUpdate(self):
#         # остаток пути      /update
#         # название функции  /userInsert
#         pass
#
#     def test_HTTPServerGetMyControllerUserSelect(self):
#         # остаток пути      /select
#         # название функции  /userInsert
#         pass

#====================================================================#

    # def test_HTTPServerPostMyServerHeaders(self):
    #     (myURL, myBody, myHeader) = fx.fixturePostPath(9)
    #     req = requests.post(myURL, json=myBody, headers=myHeader)
    #     path = req.url.split("/")[3:6]
    #     print(" =№3= THIS IS test_HTTPServerPath = ", path)
    #     print(" =№3= THIS IS test_HTTPServerPath = ", myURL.split("/")[3:6])
    #     self.assertEqual(req.url, myURL)
    #     self.assertEqual(path, myURL.split("/")[3:6])
    #     self.assertEqual(path, myURL.split("/")[3:6])


    # def test_HTTPServerJSON(self):
    #     (myURL, myBody, myHeader, codeSuccessful) = fx.fixturePostURL(9)
    #     req = requests.post(myURL, myBody)
    #     print("  THIS IS TEST json - REQ.JSON = ", req.json())
    #     self.assertEqual(req.json(), myBody)

    # r.status_code
    # r.json()

    # url = "http://localhost:8080"
    # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)

    # 1. путь
    # 2. тело в формате json
    # 3. заголовки)

myTest = myTestHTTPServer()

myTest.test_HTTPServerPostMyServerCODE200()
myTest.test_HTTPServerPostMyServerURL()
myTest.test_HTTPServerPostMyServerPath()
myTest.test_HTTPServerPostMyServerBody()

myTest.test_HTTPServerGetMyServerCODE200()
myTest.test_HTTPServerGetMyServerURL()
myTest.test_HTTPServerGetMyServerPath()


if __name__ == '__main__':
    unittest.main()
