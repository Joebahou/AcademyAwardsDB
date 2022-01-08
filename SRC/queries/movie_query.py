from SRC import db_connector


def getMovieByName(movieTitle):
    query = f""" SELECT  title,
                        budget, 
                        overview,
                        original_language,
                        popularity,
                        release_date,
                        revenue,
                        vote_average,
                        vote_count        
                FROM movie 
                WHERE title = "{movieTitle}" """
    movies_from_db = db_connector.getFromDB(query)
    for movie in movies_from_db:
        print("title = ", movie[0], )
        print("Budget = ", movie[1])
        print("Overview  = ", movie[2])
        print("Original language = ", movie[3])
        print("Popularity  = ", movie[4])
        print("Release date  = ", movie[5])
        print("Revenue  = ", movie[6])
        print("Vote average  = ", movie[7])
        print("Vote count   = ", movie[8], "\n")
    return movies_from_db


def getMovieGenres(movieTitle):
    query = f"""SELECT g.genre FROM movie as m,genre as g,movie_genre as m_g 
    WHERE m.title = "{movieTitle}" and m.id=m_g.movie_id and m_g.genre_id=g.id"""
    genres_of_movie = db_connector.getFromDB(query)
    print("Total number of genres: ", db_connector.rowcount())
    print("\nPrinting each genre\n")
    for genre in genres_of_movie:
        print(genre[0], "\n")
    return genres_of_movie


def getMovieProdCompany(movieTitle):
    query = f"""SELECT p.name FROM movie as m,production_company as p,movie_production_company as m_p 
    WHERE m.title = "{movieTitle}" and m.id=m_p.movie_id and m_p.production_company_id=p.id"""
    prod_comp_of_movie = db_connector.getFromDB(query)
    print("Total number of production companies : ", db_connector.rowcount())
    print("\nPrinting each production company")
    for prod_comp in prod_comp_of_movie:
        print(prod_comp[0], "\n")
    return prod_comp_of_movie


def getMovieTopActors(movieTitle):
    query = f"""SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j,jobInMovie as j 
    WHERE m.title = "{movieTitle}" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and p_m_j.job_id=j.id and j.job_name="Acting" """
    person_in_movie = db_connector.getFromDB(query)
    print("Total number of actors ", db_connector.rowcount())
    print("\nPrinting each actor\n")
    for person in person_in_movie:
        print("name = ", person[0], "\n")
    return person_in_movie


def getMovieDirectors(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j,jobInMovie as j 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and p_m_j.job_id=j.id and j.job_name="Directing" """ % movieTitle
    person_in_movie = db_connector.getFromDB(query)
    print("Total number of directors", db_connector.rowcount())
    print("\nPrinting each director\n")
    for person in person_in_movie:
        print("name = ", person[0], "\n")
    return person_in_movie


def getNumOfNomination(movieTitle):
    query = f"""SELECT count(*) as numOfNomination FROM movie as m,award as a 
        WHERE m.title = "{movieTitle}" and m.id=a.movie_id """
    numOfNomination = db_connector.getFromDB(query)
    print("Total number of nominations", numOfNomination[0][0])
    return numOfNomination[0][0]


def getNomination(movieTitle):
    query = f"""SELECT o.category,a.year,a.has_won as numOfNomination FROM movie as m,award as a, oscarCategory as o
        WHERE m.title = "{movieTitle}" and m.id=a.movie_id and a.oscar_category_id=o.id """
    nominations = db_connector.getFromDB(query)

    for n in nominations:
        print("category of nomination = ", n[0])
        print("year = ", n[1])
        if n[2]:
            print("has won? = ", "yes", "\n")
        else:
            print("has won? = ", "no", "\n")
    return nominations


def getMoviesByGenre(genre_name):
    query = """SELECT m.title FROM movie as m,genre as g, movie_genre as m_g WHERE g.genre = "%s" and 
    g.id=m_g.genre_id and m_g.movie_id=m.id""" % genre_name
    movies_from_db = db_connector.getFromDB(query)
    print("Total number of movies", db_connector.rowcount())
    print("\nPrinting each movie\n")
    for movie in movies_from_db:
        print("Vote count  = ", movie[0], "\n")
    return movies_from_db


def getNumOfWins(movieTitle):
    query = f"""SELECT count(*) as numOfWins FROM movie as m,award as a 
        WHERE m.title = "{movieTitle}" and m.id=a.movie_id and a.has_won=1"""
    numOfWins = db_connector.getFromDB(query)
    print("Total number of wins", numOfWins[0][0])
    return numOfWins[0][0]


# get cast nominees for movie
def getMovieNomineesPersonals(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j, award_person as a_p, award as a 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and m.id=a.movie_id and a.id=a_p.award_id and a_p.person_id=p.id """ % movieTitle
    person_in_movie = db_connector.getFromDB(query)
    print("Total number of nominees", db_connector.rowcount())
    print("\nPrinting each actor/producers\n")
    for person in person_in_movie:
        print("name = ", person[0], "\n")
    return person_in_movie


# get oscar winnig cast for movie
def getMovieAwardWinningPersonals(movieTitle):
    query = """SELECT p.name FROM movie as m,person as p,person_movie_job as p_m_j, award_person as a_p, award as a 
    WHERE m.title = "%s" and m.id=p_m_j.movie_id and p_m_j.person_id=p.id and m.id=a.movie_id and a.id=a_p.award_id and a_p.person_id=p.id and a.has_won= 1 """ % movieTitle
    person_in_movie = db_connector.getFromDB(query)
    print("Total number of award winning actors and producers", db_connector.rowcount())
    print("\nPrinting each actor/producers\n")
    for person in person_in_movie:
        print("name = ", person[0], "\n")
    return person_in_movie
