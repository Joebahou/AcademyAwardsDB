from SRC import db_connector


def getMovieByName(movieTitle):
    query = """SELECT * FROM movie WHERE title = "%s" """ % movieTitle
    movies_from_db = db_connector.getFromDB(query)
    for movie in movies_from_db:
        print("title = ", movie[1], )
        print("Budget = ", movie[2])
        print("Overview  = ", movie[3])
        print("Original language = ", movie[4])
        print("Popularity  = ", movie[5])
        print("Release date  = ", movie[6])
        print("Revenue  = ", movie[7])
        print("Vote average  = ", movie[8])
        print("Vote count   = ", movie[9], "\n")


def getMovieGenres(movieTitle):
    query = """SELECT g.genre FROM movie as m,genre as g,movie_genre as m_g 
    WHERE m.title = "%s" and m.id=m_g.movie_id and m_g.genre_id=g.id""" % movieTitle
    genres_of_movie = db_connector.getFromDB(query)
    print("Total number of genres: ", db_connector.rowcount())
    print("\nPrinting each genre\n")
    for genre in genres_of_movie:
        print(genre[0], "\n")


def getMovieProdCompany(movieTitle):
    query = """SELECT p.name FROM movie as m,production_company as p,movie_production_company as m_p 
    WHERE m.title = "%s" and m.id=m_p.movie_id and m_p.production_company_id=p.id""" % movieTitle
    prod_comp_of_movie = db_connector.getFromDB(query)
    print("Total number of production companies : ", db_connector.rowcount())
    print("\nPrinting each production company")
    for prod_comp in prod_comp_of_movie:
        print(prod_comp[0], "\n")


def getMovieTopActors(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j,jobInMovie as j 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and p_m_j.job_id=j.id and j.job_name="Acting" """ % movieTitle
    Person_in_movie = db_connector.getFromDB(query)
    print("Total number of actors ", db_connector.rowcount())
    print("\nPrinting each actor\n")
    for person in Person_in_movie:
        print("name = ", person[0], "\n")


def getMovieDirectors(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j,jobInMovie as j 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and p_m_j.job_id=j.id and j.job_name="Directing" """ % movieTitle
    person_in_movie = db_connector.getFromDB(query)
    print("Total number of directors", db_connector.rowcount())
    print("\nPrinting each director\n")
    for person in person_in_movie:
        print("name = ", person[0], "\n")


def getNumOfNomination(movieTitle):
    query = """SELECT count(*) as numOfNomination FROM movie as m,award as a 
        WHERE m.title = "%s" and m.id=a.movie_id """ % movieTitle
    numOfNomination = db_connector.getFromDB(query)
    print("Total number of nominations", numOfNomination[0][0])


def getNomination(movieTitle):
    query = """SELECT o.category,a.year,a.has_won as numOfNomination FROM movie as m,award as a, oscarCategory as o
        WHERE m.title = "%s" and m.id=a.movie_id and a.oscar_category_id=o.id """ % movieTitle
    Nominations = db_connector.getFromDB(query)

    for n in Nominations:
        print("category of nomination = ", n[0])
        print("year = ", n[1])
        if n[2]:
            print("has won? = ", "yes", "\n")
        else:
            print("has won? = ", "no", "\n")


def getMoviesByGenre(genre_name):
    query = """SELECT m.title FROM movie as m,genre as g, movie_genre as m_g WHERE g.genre = "%s" and 
    g.id=m_g.genre_id and m_g.movie_id=m.id""" % genre_name
    movies_from_db = db_connector.getFromDB(query)
    print("Total number of movies", db_connector.rowcount())
    print("\nPrinting each movie\n")
    for movie in movies_from_db:
        print("Vote count  = ", movie[0], "\n")


def getNumOfWins(movieTitle):
    query = """SELECT count(*) as numOfWins FROM movie as m,award as a 
        WHERE m.title = "%s" and m.id=a.movie_id and a.has_won=1""" % movieTitle
    numOfWins = db_connector.getFromDB(query)
    print("Total number of wins", numOfWins[0][0])


# get cast nominees for movie
def getMovieNomineesPersonals(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j, award_person as a_p, award as a 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and m.id=a.movie_id and a.id=a_p.award_id and a_p.person_id=p.id """ % movieTitle
    Person_in_movie = db_connector.getFromDB(query)
    print("Total number of nominees", db_connector.rowcount())
    print("\nPrinting each actor/producers\n")
    for person in Person_in_movie:
        print("name = ", person[0], "\n")


# get oscar winnig cast for movie
def getMovieAwardWinningPersonals(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j, award_person as a_p, award as a 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and m.id=a.movie_id and a.id=a_p.award_id and a_p.person_id=p.id and a.has_won= 1 """ % movieTitle
    Person_in_movie = db_connector.getFromDB(query)
    print("Total number of award winning actors and producers", db_connector.rowcount())
    print("\nPrinting each actor/producers\n")
    for person in Person_in_movie:
        print("name = ", person[0], "\n")
