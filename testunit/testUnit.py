import unittest
from fixtures import fixtures as fx
from mycontroller import MyController
import requests
import json

class myTestHTTPServer(unittest.TestCase):

#     def test_HTTPServerPostMyServerCODE200(self):
#         (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
#         req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
#         self.assertEqual(req.status_code, codeSuccessful)
#
#     def test_HTTPServerPostMyServerURL(self):
#         (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
#         req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
#         self.assertEqual(req.url, myURL+myPath)
#
#     def test_HTTPServerPostMyServerPath(self):
#         (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
#         req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
#         path = req.text.split("?")[0]
#         self.assertEqual(path, myPath)
#
#     def test_HTTPServerPostMyServerBody(self):
#         (myURL, myPath, myBody, myHeader, codeSuccessful) = fx.fixtureHTTPPost(9)
#         req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
#         body = req.text.split("?")[1]
#         self.assertEqual(body, json.dumps(myBody))
#
# #==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==GET==#
#
#     def test_HTTPServerGetMyServerCODE200(self):
#         (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
#         req = requests.get(myURL+myPath)
#         self.assertEqual(req.status_code, codeSuccessful)
#
#     def test_HTTPServerGetMyServerURL(self):
#         (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
#         req = requests.get(myURL+myPath)
#         self.assertEqual(req.url, myURL+myPath)
#
#     def test_HTTPServerGetMyServerPath(self):
#         (myURL, myPath, codeSuccessful) = fx.fixtureHTTPGet(9)
#         req = requests.get(myURL+myPath)
#         path = req.text
#         self.assertEqual(path, myPath)

#==insert==update==select==delete==insert==update==select==delete==#

    def test_HTTPServerPostMyControllerUserInsert(self):
        (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserInsert(9)
        req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
        # path = req.text.split("?")[0]
        # pathSplit = path.split("/")
        # pathRest = str(pathSplit[2]) + str("/") + str(pathSplit[3])
        myController = MyController()
        pathUserInsert = myController.myPath
        print(pathUserInsert)
        self.assertEqual(pathUserInsert, response)

    # def test_HTTPServerPostMyControllerUserUpdate(self):
    #     (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserUpdate(9)
    #     req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
    #     path = req.text.split("?")[0]
    #     pathSplit = path.split("/")
    #     pathRest = str(pathSplit[2]) + str("/") + str(pathSplit[3])
    #     myController = MyController()
    #     pathUserUpdate = myController.userUpdate(pathRest)
    #     self.assertEqual(pathUserUpdate, response)
    #
    # def test_HTTPServerPostMyControllerUserSelect(self):
    #     (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserSelect(9)
    #     req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
    #     path = req.text.split("?")[0]
    #     pathSplit = path.split("/")
    #     pathRest = str(pathSplit[2]) + str("/") + str(pathSplit[3])
    #     myController = MyController()
    #     pathUserSelect = myController.userSelect(pathRest)
    #     self.assertEqual(pathUserSelect, response)
    #
    # def test_HTTPServerPostMyControllerUserDelete(self):
    #     (myURL, myPath, myBody, myHeader, response) = fx.fixtureHTTPPostUserDelete(9)
    #     req = requests.post(myURL+myPath, json=myBody, headers=myHeader)
    #     path = req.text.split("?")[0]
    #     pathSplit = path.split("/")
    #     pathRest = str(pathSplit[2]) + str("/") + str(pathSplit[3])
    #     myController = MyController()
    #     pathUserDelete = myController.userDelete(pathRest)
    #     self.assertEqual(pathUserDelete, response)


myTest = myTestHTTPServer()

# myTest.test_HTTPServerPostMyServerCODE200()
# myTest.test_HTTPServerPostMyServerURL()
# myTest.test_HTTPServerPostMyServerPath()
# myTest.test_HTTPServerPostMyServerBody()
# myTest.test_HTTPServerGetMyServerCODE200()
# myTest.test_HTTPServerGetMyServerURL()
# myTest.test_HTTPServerGetMyServerPath()
# myTest.test_HTTPServerPostMyControllerUserInsert()
# myTest.test_HTTPServerPostMyControllerUserUpdate()
# myTest.test_HTTPServerPostMyControllerUserSelect()
# myTest.test_HTTPServerPostMyControllerUserDelete()


if __name__ == '__main__':
    unittest.main()