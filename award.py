def addAwardQuery(year, category_id, movie_id, has_won):
    return """INSERT INTO award (year, oscar_category_id, movie_id, has_won)
     VALUES (%s,%s,%s,%s)""" % \
                   (year, category_id, movie_id, has_won)

class Award:
    def __init__(self, year, category_id, movie_id, has_won, award_id=0):
        self.year = year
        self.category_id = category_id
        self.movie_id = movie_id
        self.has_won = has_won
        self.id = award_id
