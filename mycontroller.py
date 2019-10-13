# -*- coding: utf-8 -*-

from dao import DAO

class MyController:
    def __init__(self):
        self.dataAccessObject = DAO()

    def requestsToDB(self, path, body):
        pathSplit = path.split("/")
        lastPath = str(pathSplit[2]) + str("/") + str(pathSplit[3])

        if pathSplit[1] == "users":
            if pathSplit[2] == "insert":
                return self.userInsert(lastPath)
            elif pathSplit[2] == "update":
                return self.userUpdate(lastPath)
            elif pathSplit[2] == "select":
                return self.userSelect(lastPath)
            elif pathSplit[2] == "delete":
                return self.userDelete(lastPath)

    def userInsert(self, lastPath):
        return str(lastPath) + "/userInsert"

    def userUpdate(self, lastPath):
        return str(lastPath) + "/userUpdate"

    def userSelect(self, lastPath):
        return str(lastPath) + "/userSelect"

    def userDelete(self, lastPath):
        return str(lastPath) + "/userDelete"
