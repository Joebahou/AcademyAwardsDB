import sys

import mysql.connector
from mysql.connector import errorcode


def getFromDB(query, val=None, size=0):
    try:
        if not val:
            DBConnector.cursor.execute(query)
            if size == 0:
                return DBConnector.cursor.fetchall()
            else:
                return DBConnector.cursor.fetchmany(size)
        else:
            DBConnector.cursor.execute(query, val)
            if size == 0:
                return DBConnector.cursor.fetchall()
            else:
                return DBConnector.cursor.fetchmany(size)
    except mysql.connector.Error as err:
        print("error in getFromDB:")
        print(err.msg)
        print("query: ", query)
        return []


def getLastInsertedId():
    return DBConnector.cursor.lastrowid


def rowcount():
    return DBConnector.cursor.rowcount


def insertToDB(query):
    try:
        DBConnector.cursor.execute(query)
        DBConnector.cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print("error in insertToDB:")
            print(err.msg)
            print("query: ", query)
            # Rollback in case there is any error
            DBConnector.cnx.rollback()


def insertToDBWithVal(query, val=None):
    if val is None:
        try:
            DBConnector.cursor.execute(query)
            DBConnector.cnx.commit()
        except mysql.connector.Error as err:
            print("error in queryToDB:")
            print(err.msg)
            print("query: ", query)
            # Rollback in case there is any error
            DBConnector.cnx.rollback()
    else:
        try:
            DBConnector.cursor.execute(query, val)
            DBConnector.cnx.commit()
        except mysql.connector.Error as err:
            print("error in queryToDB:")
            print(err.msg)
            print("query: ", query)
            # Rollback in case there is any error
            DBConnector.cnx.rollback()


def create_table(table_name, table_description):
    try:
        print("Creating table {}: ".format(table_name), end='')
        DBConnector.cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def try_create_db():
    try:
        DBConnector.cursor.execute("USE {}".format(DBConnector.DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DBConnector.DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database()
            print("Database {} created successfully.".format(DBConnector.DB_NAME))

        else:
            print("err")
            exit(1)


def create_database():
    try:
        DBConnector.cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DBConnector.DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def closeConnection():
    try:
        DBConnector.cursor.close()
        DBConnector.cnx.close()
    except:
        print("couldn't log out to server")
        sys.exit(1)


def openConnection():
    try:
        DBConnector.cnx = mysql.connector.connect(
            host="localhost",
            user="DbMysql34",
            password="DbMysql34",
            port=3305
        )
        DBConnector.cnx.database = DBConnector.DB_NAME
        DBConnector.cursor = DBConnector.cnx.cursor()
    except:
        print("couldn't log in to server")
        sys.exit(1)


class DBConnector:
    cnx = None
    cursor = None
    DB_NAME = 'DbMysql34'
