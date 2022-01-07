import csv

from . import award
from . import categories
from . import movie
from . import person
from SRC import db_connector

from .person import *
from .categories import *


def retrieveMoviesAndPersonsFromCSV():
    addCategoriesToDB()

    file = open("movies2.csv", encoding="utf8", errors="ignore")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        print(row)
        addMovieToDB(row)
        addPersonToDB(row)
        addAwardToDB(row)

    file.close()


def addMovieToDB(row):
    if not isInCategories(row[1]):
        return
    title = getTitleFromRow(row)
    if not movie.isMovieExistsInDB(title):
        add_movie = """INSERT INTO movie (title) VALUES ("%s")""" % title
        db_connector.insertToDB(add_movie)
        return


def addPersonToDB(row):
    names = getPersonsFromRow(row)
    if len(names) == 0:
        return

    for name in names:
        if not isPersonExistsInDB(name):
            checkRegularName(name)
            add_person = """INSERT INTO person (name) VALUES ("%s")""" % name
            db_connector.insertToDB(add_person)
    return


def checkRegularName(name):
    not_regular_name = False
    name_split = name.split(" ")
    # if len(name_split) > 2:
    #     not_regular_name = True
    for sub_name in name_split:
        if not sub_name.isalpha():
            not_regular_name = True
    if not_regular_name:
        print("****** not regular name: ", name)


def addCategoryToDB(category):
    if not isCategoryExistsInDB(category):
        add_category = """INSERT INTO oscarCategory (category) VALUES ("%s")""" % category
        db_connector.insertToDB(add_category)


def addCategoriesToDB():
    for category in Categories.categoriesForMovies:
        addCategoryToDB(category)

    for category in Categories.categoriesForPerson:
        addCategoryToDB(category)


def addAwardToDB(row):
    category = row[1]
    if not isInCategories(category):
        return
    title = getTitleFromRow(row)
    movie_id = movie.getMoviesByName(title)[0].id
    category_id = categories.getCategoriesByName(category)[0].category_id
    year = getYearFromRow(row)
    won = getWonFromRow(row)
    query = award.addAwardQuery(year, category_id, movie_id, won)
    db_connector.insertToDB(query)
    persons = getPersonsFromRow(row)
    award_id = db_connector.getLastInsertedId()
    for person_db in persons:
        person_id = person.getPersonsByName(person_db)[0].person_id
        query = award.addAwardPersonQuery(award_id, person_id)
        db_connector.insertToDB(query)


def getWonFromRow(row):
    if row[4] == "YES":
        return 1
    return 0


def getYearFromRow(row):
    return row[0].split(" (")[0]


def getTitleFromRow(row):
    category = row[1]
    if (category in Categories.categoriesForMovies) or (category == Directing):
        title = row[2]
    else:
        title = row[3].split(" {")[0]
    return title


name_saparator = ' and '


def getPersonsFromRow(row):
    category = row[1]
    if category in Categories.categoriesForPerson:
        if category == Directing:
            return row[3].split(name_saparator)
        else:
            return row[2].split(name_saparator)
    else:
        return []


def getNumOrZeroIfNone(num):
    if num[0][0] is None:
        return 0
    else:
        return num[0][0]



