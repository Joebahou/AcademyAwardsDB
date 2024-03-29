from SRC import db_connector

def create_fulltext_indices():
    full_text_index_movie="""CREATE FULLTEXT INDEX title_fulltext ON movie(title)"""
    db_connector.insertToDB(full_text_index_movie)


def create_indices():
    person_index="""CREATE  INDEX name_idx ON person(name) USING HASH """
    award_index = """CREATE  INDEX award_idx ON award(id,year) USING BTREE """
    movie_index="""CREATE  INDEX title_idx ON movie(title) USING HASH  """
    movie_job_index = """CREATE  INDEX movie_job_idx ON person_movie_job(movie_id,job_id) USING HASH"""
    db_connector.insertToDB(person_index)
    db_connector.insertToDB(award_index)
    db_connector.insertToDB(movie_index)
    db_connector.insertToDB(movie_job_index)


