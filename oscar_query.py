import db_connector


def getMovieMaxBudget(min_year,max_year,only_winners=False,categories_list=[],genres_list=[]):
    min_year_query=getQueryAwardMinYear(min_year)
    max_year_query=getQueryAwardMaxYear(max_year)
    genre_query=getQueryGenres(genres_list)
    category_query=getQueryCategories(categories_list)
    query="""SELECT title,budget  FROM movie as m,award as a WHERE m.id=a.movie_id and  """





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