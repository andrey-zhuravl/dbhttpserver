# -*- coding: utf-8 -*-

from dao import DAO
from contextlib import closing

class MyController:
    def __init__(self):
        self.dataAccessObject = DAO()

    def requestsToDB(self, path, bodyJson):
        print('path = ', path)

        header = path.split("/")
        lastPath = str(header[2]) + str("/") + str(header[3])
        print("lastPath = ", lastPath)
        print(" header = path.split(/) = ", header)

        print("    RRR  bodyJson - body.json() = ", bodyJson)
        print("    RRR  тип данных - body.json() = ", type(bodyJson))

        if header[1] == "users":
            userID = header[3]
            if header[2] == "insert":
                print("  Class MyController, if header == users-insert, header[1]  = ", header[1])
                print("  Class MyController, if header == users-insert, header[2]  = ", header[2])
                print("  Class MyController, if header == users-insert, header[3]  = ", header[3])
                self.userInsert(lastPath)
            elif header[2] == "update":
                print("  Class MyController, if header == users-update, header[1]  = ", header[1])
                print("  Class MyController, if header == users-update, header[2]  = ", header[2])
                print("  Class MyController, if header == users-update, header[3]  = ", header[3])
                self.userUpdate(lastPath)
            # elif header[2] == "select":
            #     self.userSelect(userID)
            # elif header[2] == "delete":
            #     self.userDelete(userID)
        return path, bodyJson


    def userInsert(self, lastPath):
        print("def userInsert --- ", str(lastPath) + "/userInsert")

    def userUpdate(self, lastPath):
        print("def userUpdate - ", str(lastPath) + "/userUpdate")
    #
    # def userSelect(self, userID):
    #     self.dataAccessObject.selectData(userID)

    # def userInsert(self, header):
    #     print("def userInsert - ", str(header) + "userInsert")
    #
    # def userUpdate(self, header):
    #     print("def userUpdate - ", str(header) + "userUpdate")
    #
    # def userSelect(self, header):
    #     print("def userSelect - ", str(header) + "userSelect")

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
