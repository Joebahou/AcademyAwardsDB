import mysql.connector
from mysql.connector import errorcode


def getFromDB(query, size=0):
    try:
        DBConnector.cursor.execute(query)
        if size == 0:
            return DBConnector.cursor.fetchall()
        else:
            return DBConnector.cursor.fetchmany(size)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)


def getLastInsertedId():
    return DBConnector.cursor.lastrowid


def insertToDB(query):
    try:
        DBConnector.cursor.execute(query)
        DBConnector.cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)


def closeConnection():
    DBConnector.cursor.close()
    DBConnector.cnx.close()


def openConnection():
    DBConnector.cnx = mysql.connector.connect(
        host="localhost",
        user="DbMysql34",
        password="DbMysql34",
        port=3305
    )
    DBConnector.cnx.database = DBConnector.DB_NAME
    DBConnector.cursor = DBConnector.cnx.cursor()


class DBConnector:
    cnx = None
    cursor = None
    DB_NAME = 'DbMysql34'
