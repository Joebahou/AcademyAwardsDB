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


def insertToDB(query):
    try:
        DBConnector.cursor.execute(query)
        DBConnector.cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)


class DBConnector:
    cnx = mysql.connector.connect(
        host="localhost",
        user="DbMysql34",
        password="DbMysql34",
        port=3305
    )

    DB_NAME = 'DbMysql34'

    cnx.database = DB_NAME

    cursor = cnx.cursor()
