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

def updateMovie(movie_db_id,budget, overview, original_language,popularity,release_date,revenue,vote_avg,vote_count,db_id):
    sql = "UPDATE movie SET budget = %s WHERE address = %s"
    val = ("Valley 345", "Canyon 123")

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


def getLowestMovieID():
    query = """SELECT MIN(id) FROM movie"""
    highest_id = db_connector.getFromDB(query)
    return utils.getNumOrZeroIfNone(highest_id)