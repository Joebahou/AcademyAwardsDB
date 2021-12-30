import db_connector


def addAwardQuery(year, category_id, movie_id, has_won):
    return """INSERT INTO award (year, oscar_category_id, movie_id, has_won)
     VALUES (%s,%s,%s,%s)""" % \
           (year, category_id, movie_id, has_won)


def addAwardPersonQuery(award_id, person_id):
    return """INSERT INTO award_person (award_id,person_id) VALUES(%s,%s)""" % (award_id, person_id)

def getMovieAwardYear(movie_id):
    query =("SELECT year FROM award WHERE movie_id= (%s) ") % movie_id
    award_1= db_connector.getFromDB(query,1)
    award_year=award_1[0][0]
    return award_year

class Award:
    def __init__(self, year, category_id, movie_id, has_won, person=None, award_id=0):
        self.person = person
        self.year = year
        self.category_id = category_id
        self.movie_id = movie_id
        self.has_won = has_won
        self.id = award_id
