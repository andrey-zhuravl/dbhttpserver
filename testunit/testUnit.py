import unittest
from fixtures import fixtures as fx
from mycontroller import MyController
import requests
import json
from dao import DAO


class myTestHTTPServer(unittest.TestCase):

    def test_HTTPServerPostMyServerCODE200(self):
        (myURL, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL, json=myBody, headers=myHeader)
        self.assertEqual(req.status_code, codeSuccessful)

    def test_HTTPServerPostMyServerURL(self):
        (myURL, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
        req = requests.post(myURL, json=myBody, headers=myHeader)
        self.assertEqual(req.url, myURL)

#     def test_HTTPServerPostMyServerPath(self):
#         (myURL, myBody, myHeader, codeSuccessful) = fx.fixturePostPath(9)
#         req = requests.post(myURL, json=myBody, headers=myHeader)
#         path = req.url.split("/")[3:6]
#         responseFromHTTP = MyController()
#         responseFromHTTP.requestsToDB(req.url.split("/"))
#         self.assertEqual(req.url, myURL)
#         self.assertEqual(path, myURL.split("/")[3:6])
#         self.assertEqual(path, myURL.split("/")[3:6])
#
#     def test_HTTPServerPostMyServerHeaders(self):
#         (myURL, myBody, myHeader) = fx.fixturePostPath(9)
#         req = requests.post(myURL, json=myBody, headers=myHeader)
#         path = req.url.split("/")[3:6]
#         print(" =№3= THIS IS test_HTTPServerPath = ", path)
#         print(" =№3= THIS IS test_HTTPServerPath = ", myURL.split("/")[3:6])
#         responseFromHTTP = MyController()
#         responseFromHTTP.requestsToDB(req.url.split("/"))
#         self.assertEqual(req.url, myURL)
#         self.assertEqual(path, myURL.split("/")[3:6])
#         self.assertEqual(path, myURL.split("/")[3:6])
#
#     def test_HTTPServerPostMyServerBody(self):
#
#         pass
#
#     def test_HTTPServerPostMyControllerUserInsert(self):
#         # остаток пути      /insert
#         # название функции  /userInsert
#         pass
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
# #==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==#
#
#     def test_HTTPServerGetMyServerCODE200(self):
#         (myURL, myBody, codeSuccessful) = fx.fixturePostStatusCode(9)
#         req = requests.get(myURL, json=myBody, headers=myHeader)
#         print(req.status_code)
#         print(" =№1= THIS IS TEST code 200 = ", req.status_code)
#         responseFromHTTP = MyController()
#         responseFromHTTP.requestsToDB(req.url, myBody)
#         self.assertEqual(req.status_code, codeSuccessful)
#
#     def test_HTTPServerGetMyServerURL(self):
#         (myURL, myBody, myHeader, codeSuccessful) = fx.fixturePostURL(9)
#         req = requests.get(myURL, json=myBody, headers=myHeader)
#         print(" =№2= THIS IS TEST URL - REQ.URL = ", req.url)
#         responseFromHTTP = MyController()
#         responseFromHTTP.requestsToDB(req.url.split("/"))
#         self.assertEqual(req.url, myURL)
#
#     def test_HTTPServerGetMyServerPath(self):
#         (myURL, myBody, myHeader) = fx.fixturePostPath(9)
#         req = requests.get(myURL, json=myBody, headers=myHeader)
#         path = req.url.split("/")[3:6]
#         print(" =№3= THIS IS test_HTTPServerPath = ", path)
#         print(" =№3= THIS IS test_HTTPServerPath = ", myURL.split("/")[3:6])
#         responseFromHTTP = MyController()
#         responseFromHTTP.requestsToDB(req.url.split("/"))
#         self.assertEqual(req.url, myURL)
#         self.assertEqual(path, myURL.split("/")[3:6])
#         self.assertEqual(path, myURL.split("/")[3:6])
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

# myTest = myTestHTTPServer()
#
# myTest.test_HTTPServerCODE200()
# myTest.test_HTTPServerPath()
# myTest.test_HTTPServerURL()

if __name__ == '__main__':
    unittest.main()
