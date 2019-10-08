# -*- coding: utf-8 -*-

from dao import DAO
from contextlib import closing

class MyController:
    def __init__(self):
        pass
        self.dataAccess = DAO()

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


    def userInsert(self, userID):
        self.dataAccess.insertData(userID)

    def userUpdate(self, userID):
        self.dataAccess.updateData(userID)

    def userSelect(self, userID):
        self.dataAccess.selectData(userID)

    def userDelete(self, userID):
        self.dataAccess.deleteData(userID)

    def openDB(self):
        pass

    def dropCollumn(self):
        pass

    def dropTable(self):
        pass

    def addCollumn(self):
        pass

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
