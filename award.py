def addAwardQuery(year, category_id, movie_id, has_won):
    return """INSERT INTO award (year, oscar_category_id, movie_id, has_won)
     VALUES (%s,%s,%s,%s)""" % \
           (year, category_id, movie_id, has_won)


def addAwardPersonQuery(award_id, person_id):
    return """INSERT INTO award_person (award_id,person_id) VALUES(%s,%s)""" % (award_id, person_id)

def getMovieAwardYear():
    pass


class Award:
    def __init__(self, year, category_id, movie_id, has_won, person=None, award_id=0):
        self.person = person
        self.year = year
        self.category_id = category_id
        self.movie_id = movie_id
        self.has_won = has_won
        self.id = award_id
