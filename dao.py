# -*- coding: utf-8 -*-

from contextlib import closing
import psycopg2
import postgresql

from math import *

class DAO:

    def __init__(self):
        pass

    def openDB(self, DBName):
        # db_traindb = postgresql.open('pq://postgres:postgres@localhost:5432/'+'DBName')
        # db_neurodb = postgresql.open('pq://postgres:postgres@localhost:5432/'+'DBName')
        pass

    def insertData(self, nameID):
        print("THIS IS DAO - insertData, nameID = ", nameID)
        # ins = db_traindb.prepare("INSERT INTO users (user_name) VALUES ($1)")
        # for i in range(1,4,1):
        #     ins("Marko"+str(i))
        return nameID
        pass

    def updateData(self, nameID):
        # update = db_traindb.prepare("UPDATE city SET id_country = $2 WHERE city = $1")
        # update("Toronto", 55)
        # update("Palermo", 56)
        # update("Armant", 57)

        # update = db_traindb.prepare("UPDATE users SET salary = $2 WHERE user_name = $1")
        # for i in range(1, 4, 1):
        #     update("Marko" + str(i), 3000 * i)
        # for i in range(1, 5, 1):
        #     update("Ramses" + str(i), 2000 * i)
        # for i in range(1, 5, 1):
        #     update("Daniel" + str(i), 1000 * i)
        pass

    def selectData(self, nameID):
        # sel = db_traindb.query("SELECT * FROM public.users")

        # sel = db_traindb.query("SELECT users.user_name AS usr, users.salary, city.city AS ct, country.country AS cntr "
        #                        "FROM public.users "
        #                        "LEFT OUTER JOIN city ON users.id_city = city.id "
        #                        "LEFT OUTER JOIN country ON city.id_country = country.id "
        #                        "ORDER BY salary;")
        # print(db_traindb.query('select * from country'))

        # print(db_traindb.query("SELECT * FROM public.country AS cnt, public.city AS ct, public.users AS usr "
        #                          "WHERE (cnt.id = ct.id_country AND usr.id_city = ct.id)"))

        # sel = db_traindb.query("SELECT country, city, user_name, salary "
        #                        "FROM public.country AS cnt, public.city AS ct, public.users AS usr "
        #                        "WHERE cnt.id = ct.id_country AND ct.id = usr.id_city "
        #                        "ORDER BY user_name")
        pass

    def deleteData(self, nameID):
        # delete = db_traindb.prepare("DELETE FROM country WHERE id = $1")
        # for i in range(49, 52, 1):
        #     delete(i)
        pass

    def dropCollumn(self, collumnName):
        # drop = db_traindb.prepare("ALTER TABLE country DROP COLUMN country3")
        # drop("country3")
        # drop("country4")

        # for i in range(3,4,1):
        #     drop("country"+str(i))
        pass

    def dropTable(self, tableName):
        # db_traindb.execute("DROP TABLE employee")
        pass

    def addCollumn(self, tableName, collumnName):
        # try:
        #     db_traindb.execute("ALTER TABLE country ADD COLUMN country text")
        # except Exception as err:
        #     print("Oops! Something was wrong. Try again...", err)
        pass

#----------------------------------------------------------------------------------#

    # def insertOneRecord(self, myCursor, id, cfill, cback, width):
    #     myCursor.execute('INSERT INTO public.shape '
    #                      'VALUES (%s, %s, %s, %s)',
    #                      (id, cfill, cback, width))
    #
    # def selectShapeAllRow(self, myCursor):
    #     myCursor.execute('SELECT * FROM public.shape')
    #     self.records = myCursor.fetchall()
    #
    # def printCursor(self, myCursor):
    #     self.selectShapeAllRow(myCursor)
    #     for row in self.records:
    #         print(row)
    #
    # def updateOneRowInShape(self, myCursor, idNew, cfill, cback, width, idOld):
    #     myCursor.execute('UPDATE public.shape '
    #                      'SET id=%s, cfill=%s, cback=%s, width=%s WHERE id = %s',
    #                      (idNew, cfill, cback, width, idOld))
    #
    # def addPsycopg2(self, id, square):
    #     # square = Square(255, 0)
    #     with closing(psycopg2.connect(dbname="neurodb",
    #                                   user="postgres",
    #                                   password="postgres",
    #                                   host="localhost")) as db:
    #         with db.cursor() as myCursor:
    #             db.autocommit = True
    #             # self.updateOneRowInShape(myCursor,
    #             #                          101,
    #             #                          int(self.colorFill),
    #             #                          int(self.colorBackground),
    #             #                          square[0],
    #             #                          5)
    #
    #             # self.insertOneRecordToEndTable(myCursor, 112, 202,303, 404)
    #
    #             print(square[0])
    #
    #             self.insertOneRecordToEndTable(myCursor,
    #                                            id,
    #                                            (self.colorFill),
    #                                            (self.colorBackground),
    #                                            square[0])
    #             self.selectShapeAllRow(myCursor)
    #             self.printCursor(myCursor)
    #
    # def addPostgresql(self, id, square):
    #     # db = postgresql.open('localhost:5432/mydb')
    #     with closing(postgresql.open('pq://postgres:postgres@localhost:5432/neurodb')) as db:
    #         db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, "
    #                    "login CHAR(64), password CHAR(64))")
    #
    #             print(square[0])
    #
    #             self.insertOneRecordToEndTable(myCursor,
    #                                            id,
    #                                            (self.colorFill),
    #                                            (self.colorBackground),
    #                                            square[0])
    #             self.selectShapeAllRow(myCursor)
    #             self.printCursor(myCursor)
