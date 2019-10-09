# -*- coding: utf-8 -*-

from dao import DAO
from contextlib import closing

class MyController:
    def __init__(self):
        self.dataAccessObject = DAO()

    def requestsToDB(self, path, bodyJson):
        header = path.split("/")
        # data = bodyJson.dumps(body)
        print("    RRR  bodyJson - body.json() = ", bodyJson)
        print("    RRR  тип данных - body.json() = ", type(bodyJson))
        print("    RRR  request = ", header)

        if header[1] == "users":
            userID = header[3]
            if header[2] == "insert":
                print("  header[1]  = ", header[1])
                print("  header[2]  = ", header[2])
                print("  header[3]  = ", header[3])
                self.userInsert(userID)
            elif header[2] == "update":
                print("  header[1]  = ", header[1])
                print("  header[2]  = ", header[2])
                print("  header[3]  = ", header[3])
                self.userUpdate(userID)
            # elif header[2] == "select":
            #     self.userSelect(userID)
            # elif header[2] == "delete":
            #     self.userDelete(userID)
        return path, bodyJson


    def userInsert(self, userID):
        self.dataAccessObject.insertData(userID)

    def userUpdate(self, userID):
        self.dataAccessObject.updateData(userID)
    #
    # def userSelect(self, userID):
    #     self.dataAccessObject.selectData(userID)
    #
    # def userDelete(self, userID):
    #     self.dataAccessObject.deleteData(userID)
    #
    # def openDB(self):
    #     pass
    #
    # def dropCollumn(self):
    #     pass
    #
    # def dropTable(self):
    #     pass
    #
    # def addCollumn(self):
    #     pass

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
