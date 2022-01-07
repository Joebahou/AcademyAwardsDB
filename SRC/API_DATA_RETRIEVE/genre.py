from SRC import db_connector


def getGenreByName(genre):
    query = """SELECT * FROM genre WHERE genre = "%s" """ % genre
    genres_from_db = db_connector.getFromDB(query)
    for genre_from_db in genres_from_db:
        genre = Genre(genre_from_db[0],genres_from_db[1])
    return genre


class Genre:
    def __init__(self, genre_id, name):
        self.name = name
        self.genre_id = genre_id
