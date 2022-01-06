def getNumOrZeroIfNone(num):
    if num[0][0] is None:
        return 0
    else:
        return num[0][0]


def getQueryGenres(genres):
    if len(genres) > 0:
        query_genre = "AND movie.id = movie_genre.movie_id AND ("
        for genre_id in genres:
            query_genre += f""" movie_genre.genre_id = {genre_id} OR """
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


def getQueryAwardWinner(only_winners):
    if only_winners:
        return "AND award.has_won = 1"
    return ""
