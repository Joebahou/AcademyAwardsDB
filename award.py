class Award:
    def __init__(self, year, category_id, movie_id, has_won, award_id=0):
        self.year = year
        self.category_id = category_id
        self.movie_id = movie_id
        self.has_won = has_won
        self.id = award_id
