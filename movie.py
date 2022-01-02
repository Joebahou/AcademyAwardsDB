import db_connector
import utils


def isMovieExistsInDB(movieTitle):
    movies = getMoviesByName(movieTitle)
    return len(movies) > 0


def getMoviesByID(id):
    query = """SELECT * FROM movie WHERE id = %s """ % id
    movies_from_db = db_connector.getFromDB(query,1)
    movie=None
    for movie_from_db in movies_from_db:
        movie = Movie(movie_from_db[0],
                      movie_from_db[1],
                      movie_from_db[2],
                      movie_from_db[3],
                      movie_from_db[4],
                      movie_from_db[5],
                      movie_from_db[6],
                      movie_from_db[7],
                      movie_from_db[8],
                      movie_from_db[9],
                      movie_from_db[10])

    return movie

def updateMovie(movie_id, overview, original_language,popularity,release_date,vote_avg,vote_count,db_id):
    sql = "UPDATE movie SET overview = %s, original_language = %s, popularity = %s, release_date = %s" \
          ", vote_average = %s, vote_count = %s, db_id = %s WHERE id = %s"
    val = (overview,original_language, popularity, release_date, vote_avg, vote_count, db_id, movie_id)
    db_connector.insertToDBWithVal(sql,val)


def getMoviesByName(movieTitle):
    query = """SELECT * FROM movie WHERE title = "%s" """ % movieTitle
    movies_from_db = db_connector.getFromDB(query)
    movies = []
    for movie_from_db in movies_from_db:
        movie = Movie(movie_from_db[0],
                      movie_from_db[1],
                      movie_from_db[2],
                      movie_from_db[3],
                      movie_from_db[4],
                      movie_from_db[5],
                      movie_from_db[6],
                      movie_from_db[7],
                      movie_from_db[8],
                      movie_from_db[9],
                      movie_from_db[10])
        movies.append(movie)
    return movies


def getHighestMovieID():
    query = """SELECT MAX(id) FROM movie"""
    highest_id = db_connector.getFromDB(query)
    return utils.getNumOrZeroIfNone(highest_id)

def getMoviesCount():
    query=("SELECT COUNT(*) FROM movie")
    return db_connector.getFromDB(query,1)[0][0]





def getLowestMovieID():
    query = """SELECT MIN(id) FROM movie"""
    highest_id = db_connector.getFromDB(query)
    return utils.getNumOrZeroIfNone(highest_id)


def insert_revenue_genres_company_prod(id,budget,revenue,genres,prod_companies,db_id):
    sql = "UPDATE movie SET budget = %s,revenue = %s WHERE db_id = %s"
    val = (budget,revenue,db_id)
    db_connector.insertToDBWithVal(sql,val)
    genre_query="INSERT IGNORE INTO genre (id,genre) VALUES (%s,%s)"
    movie_genre_query = "INSERT INTO movie_genre (movie_id, genre_id) VALUES (%s,%s)"
    for genre in genres:
        genre_id=genre["id"]
        genre_val = (genre_id,genre["name"])
        movie_genre_val = (id, genre_id)
        db_connector.insertToDBWithVal(genre_query,genre_val)
        db_connector.insertToDBWithVal(movie_genre_query, movie_genre_val)
    prod_company_query="INSERT IGNORE INTO production_company (id,name) VALUES (%s,%s)"
    movie_prod_company_query = "INSERT INTO movie_production_company (movie_id, production_company_id) VALUES (%s,%s)"
    for prod_company in prod_companies:
        prod_company_id=prod_company["id"]
        prod_company_val = (prod_company_id,prod_company["name"])
        movie_prod_company_val = (id, prod_company_id)
        db_connector.insertToDBWithVal(prod_company_query,prod_company_val)
        db_connector.insertToDBWithVal(movie_prod_company_query, movie_prod_company_val)


class Movie:
    def __init__(self, movie_id, title, budget=None, overview=None,
                 original_language="english", popularity=None,
                 release_date=None, revenue=None, vote_average=None, vote_count=None, db_id=None):
        self.db_id = db_id
        self.vote_count = vote_count
        self.vote_average = vote_average
        self.revenue = revenue
        self.release_date = release_date
        self.popularity = popularity
        self.original_language = original_language
        self.overview = overview
        self.id = movie_id
        self.title = title
        self.budget = budget








