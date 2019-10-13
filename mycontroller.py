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
                self.userInsert(lastPath)
            elif pathSplit[2] == "update":
                self.userUpdate(lastPath)
            elif pathSplit[2] == "select":
                self.userSelect(userID)
            elif pathSplit[2] == "delete":
                self.userDelete(userID)
        return path, body

    def userInsert(self, lastPath):
        return str(lastPath) + "/userInsert"

    def userUpdate(self, lastPath):
        return str(lastPath) + "/userUpdate"

    def userSelect(self, lastPath):
        return str(lastPath) + "/userSelect"

    def userDelete(self, lastPath):
        return str(lastPath) + "/userDelete"
