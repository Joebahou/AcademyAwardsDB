import csv

import movie
from categories import *
from person import getHighestPersonID, isPersonExistsInDB


def addMovieToDB(row):
    if not isInCategories(row[1]):
        return 0
    title = getTitleFromRow(row)
    if not movie.isMovieExistsInDB(title):
        movie_id = movie.getHighestMovieID() + 1
        add_movie = """INSERT INTO movie (id,title) VALUES (%s,"%s")""" % (movie_id, title)
        db_connector.insertToDB(add_movie)
        return movie_id


def addPersonToDB(row):
    names = getPersonsFromRow(row)
    person_ids = []
    if len(names) == 0:
        return person_ids

    highest_id = getHighestPersonID()
    for person in names:
        if not isPersonExistsInDB(person):
            highest_id = highest_id + 1
            add_person = """INSERT INTO person (id,name) VALUES (%s,"%s")""" % (highest_id, person)
            db_connector.insertToDB(add_person)
            person_ids.append(highest_id)
    return person_ids


def addCategoryToDB(category):
    if not isCategoryExistsInDB(category):
        highest_id = getHighestCategoryID()
        add_category = """INSERT INTO oscarCategory (id,category) VALUES (%s,"%s")""" % (highest_id + 1, category)
        db_connector.insertToDB(add_category)


def addAwardToDB(year, category_id, movie_id, has_won):
    add_category = """INSERT INTO award (year, oscar_category_id, movie_id, has_won)
     VALUES (%s,%s,%s,%s)""" % \
                   (year, category_id, movie_id, has_won)
    db_connector.insertToDB(add_category)


def addCategoriesToDB():
    for category in Categories.categoriesForMovies:
        addCategoryToDB(category)

    for category in Categories.categoriesForPerson:
        addCategoryToDB(category)


def retrieveMoviesAndPersonsFromCSV():
    addCategoriesToDB()

    file = open("academy_awards.csv", encoding="utf8", errors="ignore")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        print(row)
        addMovieToDB(row)
        addPersonToDB(row)

    file.close()


def addAwardToDB(row):
    category = row[1]
    if not isInCategories(category):
        return
    title = getTitleFromRow(row)
    movie_id = movie.getMoviesByName(title)[0].id
    year = getYearFromRow(row)
    won = getWonFromRow(row)


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
    if num[0][0] is None:
        return 0
    else:
        return num[0][0]

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
