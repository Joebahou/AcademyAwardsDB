from SRC import db_connector


def getBasicPersonInfo(person_name):
    query = f"""SELECT person.name, person.gender FROM person WHERE person.name = '{person_name}'"""
    response = db_connector.getFromDB(query)
    if len(response) > 0:
        return response[0]
    return None




def getPersonNominations(person_name, categories=[], min_year=1934, max_year=2010):
    query = getQueryNominationsByPerson(person_name, categories=categories, min_year=min_year, max_year=max_year)
    response = db_connector.getFromDB(query)

    return response


def getPersonMovies(person_name):
    query = getQueryMoviesByPerson(person_name)
    response = db_connector.getFromDB(query)
    return response


def getCountPersonNominations(person_name):
    query = getQueryNominationsByPerson(person_name)
    query_count = f"""SELECT COUNT(*) FROM ({query}) AS personNominations"""
    response = db_connector.getFromDB(query_count)

    return response[0][0]


def getCountPersonMovies(person_name):
    query = getQueryMoviesByPerson(person_name)
    query_count = f"""SELECT COUNT(*) FROM ({query}) AS personMovies"""
    response = db_connector.getFromDB(query_count)

    return response[0][0]


def getCountPersonWins(person_name):
    query = getQueryNominationsByPerson(person_name)
    query_count = f"""SELECT COUNT(*) FROM ({query}) AS personMovies WHERE won = 1"""
    response = db_connector.getFromDB(query_count)

    return response[0][0]


def getQueryMoviesByPerson(person_name):
    query = f"""    SELECT  distinct    movie.title     AS movieTitle,
                                        jobInMovie.job_name  As role
                    FROM    movie, jobInMovie, 
                            person_movie_job,
                            person
                    WHERE   person.name = "{person_name}"
                    AND     person.id = person_movie_job.person_id                                   
                    AND     person_movie_job.job_id = jobInMovie.id                                   
                    AND     person_movie_job.movie_id = movie.id                                   
                    """
    return query


def getQueryNominationsByPerson(person_name, categories=[]
                                , min_year=1934, max_year=2010):
    query = f"""    SELECT  movie.title             AS movieTitle,
                            oscarCategory.category  AS category, 
                            award.year              AS year,
                             award.has_won          AS won 
                    FROM    person, award, oscarCategory, movie, award_person
                    WHERE   person.name = "{person_name}"                
                    AND     oscarCategory.id = award.oscar_category_id 
                    AND     movie.id = award.movie_id
                    AND     person.id = award_person.person_id
                    AND     award_person.award_id = award.id
                    """
    query += "{0}{1}{2}" \
        .format(getQueryCategories(categories),
                getQueryAwardMinYear(min_year),
                getQueryAwardMaxYear(max_year))
    return query


def getQueryOnlyNominated(only_nominated):
    if only_nominated:
        return "AND     person.id = award_person.person_id \
                AND     award_person.award_id = award.id"
    else:
        return ""


def getQueryWin(only_win):
    if only_win:
        return "AND award.has_won = 1"
    return ""


def getQueryJoinMovieGenre(join):
    if join:
        return "AND movie_genre.movie_id = movie.id\n"
    return ""


def getQueryFrom_Movie_Genre(addFrom):
    if addFrom:
        return ", movie_genre\n"
    return ""


def getQueryFrom_Award_Person(addFrom):
    if addFrom:
        return ", award_person\n"
    return ""


def getQueryGenres(genres):
    if len(genres) > 0:
        query_genre = "AND ("
        for genre_id in genres:
            query_genre += f"""movie_genre.genre_id = {genre_id} OR """
        query_genre = query_genre[:-4] + ")\n"
        return query_genre
    return ""


def getQueryCategories(categories):
    if len(categories) > 0:
        query_category = "AND ("
        for category_id in categories:
            query_category += f"award.oscar_category_id = {category_id} OR "
        query_category = query_category[:-4] + ")\n"
        return query_category
    return ""


def getQueryAwardMinYear(min_year):
    if min_year > 1934:
        return "AND award.year >= %s\n" % min_year
    return ""


def getQueryAwardMaxYear(max_year):
    if max_year < 2010:
        return "AND award.year <= %s\n" % max_year
    return ""


