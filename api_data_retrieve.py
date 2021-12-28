import string

import mysql
import csv

import mysql.connector
from mysql.connector import errorcode

from categories import *


class DBRetrieveData:
    def __init__(self, cursor, cnx):
        self.cursor = cursor
        self.cnx = cnx

    def getFromDB(self, query, size=0):
        try:
            self.cursor.execute(query)
            if size == 0:
                return self.cursor.fetchall()
            elif size == 1:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchmany(size)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def insertToDB(self, query):
        try:
            self.cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def retrieveMoviesAndPersonsFromCSV(self):

        self.addCategoriesToDB()

        file = open("Salary_Data.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)
        for row in csvreader:
            self.addMovieToDB(row)
            self.addMovieToDB(row)
        file.close()

    def isMovieExistsInDB(self, movieTitle: string):
        movies = self.getMoviesByName(movieTitle)
        return len(movies) > 0

    def isPersonExistsInDB(self, personName: string):
        persons = self.getPersonsByName(personName)
        return len(persons) > 0

    def getMoviesByName(self, movieTitle: string):
        query = """SELECT * FROM movie WHERE title = '%s'""" % movieTitle
        return self.getFromDB(query, 1)

    def getPersonsByName(self, personName: string):
        query = """SELECT * FROM person WHERE name = '%s'""" % personName
        return self.getFromDB(query, 1)

    def addPersonToDB(self, row):
        names = getPersonsFromRow(row)
        if len(names) == 0:
            return

        highestId = self.getHighestPersonID()
        for person in names:
            highestId = highestId + 1
            if not self.isPersonExistsInDB(person):
                add_person = "INSERT INTO movies (movie_id,title) VALUES (%s,%s)" % (highestId, person)
                self.insertToDB(add_person)

    def addMovieToDB(self, row):
        title = getTitleFromRow(row)
        if not self.isMovieExistsInDB(title):
            highestId = self.getHighestMovieID()
            add_movie = "INSERT INTO movies (movie_id,title) VALUES (%s,%s)" % (highestId + 1, title)
            self.insertToDB(add_movie)

    def getHighestMovieID(self):
        query = """SELECT MAX(movie_id) FROM movie"""
        highestID = self.getFromDB(query, 1)
        return getNumOrZeroIfNone(highestID)

    def getHighestPersonID(self):
        query = """SELECT MAX(person_id) FROM person"""
        highestID = self.getFromDB(query, 1)
        return getNumOrZeroIfNone(highestID)

    def getHighestCategoryID(self):
        query = """SELECT MAX(id) FROM oscar_category"""
        self.cursor.execute(query)
        highestID = self.getFromDB(query, 1)
        return getNumOrZeroIfNone(highestID)

    def addCategoriesToDB(self):
        for category in Categories.categoriesForMovies:
            self.addCategoryToDB(category)

    def addCategoryToDB(self, category):
        highestId = self.getHighestCategoryID()
        add_movie = "INSERT INTO movies (movie_id,title) VALUES (%s,%s)" % (highestId + 1, category)
        self.insertToDB(add_movie)


def getTitleFromRow(row):
    category = row[1]
    if (category in Categories.categoriesForMovies) or (category == Directing):
        return row[2]
    else:
        return row[2].split(" {")[0]


def getPersonsFromRow(row):
    category = row[1]
    if category in Categories.categoriesForPerson:
        if category == Directing:
            return row[3].split(" and ")
        else:
            return row[2].split(" and ")
    else:
        return []


def getNumOrZeroIfNone(num):
    if num is None:
        return 0
    else:
        return num

# udis key = 7136f4075d33998d3d77a11a9c442439
#
# def retrieve_data_for_db():
#     api_key = "12d3cdb961e65887562f143725ee1a2b"
#     link = "https://api.themoviedb.org/3/movie/144?api_key=12d3cdb961e65887562f143725ee1a2b&language=en-US"
#     response = requests.get(link)
#
#     datetmp = response.json()
#     # getting first page
#     data = response.json()
#
#     # #appending pages 1 and 2
#     # for i in range(1, 3):
#     #     response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+api_key+"&language=en-US&page={}".format(i))
#     #     temp_df = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]
#     #     data.append(temp_df, ignore_index=False)
#
#     add_movie = "INSERT INTO movies (movie_id,title) VALUES (%(movie_id)s,%(title)s)"
#
#     row_dict = {
#         'movie_id': 1,
#         'title': data['title'],
#
#     }
#     cursor.execute(add_movie, row_dict)
#
#     cnx.commit()
#
#     # print(data.head())
