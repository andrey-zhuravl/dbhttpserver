# -*- coding: utf-8 -*-

from dao import DAO
from contextlib import closing

class MyController:
    def __init__(self):
        self.dataAccessObject = DAO()

    def requestsToDB(self, path, body):
        print('path ОТ СЕРВЕРА = ', path)

        pathSplit = path.split("/")
        lastPath = str(pathSplit[2]) + str("/") + str(pathSplit[3])

        if pathSplit[1] == "users":
            if pathSplit[2] == "insert":
                self.userInsert(lastPath)
            elif pathSplit[2] == "update":
                self.userUpdate(lastPath)
            # elif pathSplit[2] == "select":
            #     self.userSelect(userID)
            # elif pathSplit[2] == "delete":
            #     self.userDelete(userID)
        return path, body


    def userInsert(self, lastPath):
        print("def userInsert --- ", str(lastPath) + "/userInsert")

    def userUpdate(self, lastPath):
        print("def userUpdate - ", str(lastPath) + "/userUpdate")
    #
    # def userSelect(self, userID):
    #     self.dataAccessObject.selectData(userID)

    # def userInsert(self, pathSplit):
    #     print("def userInsert - ", str(pathSplit) + "userInsert")
    #
    # def userUpdate(self, pathSplit):
    #     print("def userUpdate - ", str(pathSplit) + "userUpdate")
    #
    # def userSelect(self, pathSplit):
    #     print("def userSelect - ", str(pathSplit) + "userSelect")

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
