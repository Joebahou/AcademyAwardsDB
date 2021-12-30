######################## this is joe's file to work on api, do not delete ########################

import string

import mysql
import csv

import mysql.connector
from mysql.connector import errorcode

from categories import *


class RetrieveDataApi:
    def __init__(self, cursor, cnx):
        self.cursor = cursor
        self.cnx = cnx

    def getFromDB(self, query, size=0):
        try:
            self.cursor.execute(query)
            if size == 0:
                return self.cursor.fetchall()

            else:
                if size == 1:
                    return self.cursor.fetchone()
                else:
                    return self.cursor.fetchmany(size)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def get_num_of_movies(self):
        pass



