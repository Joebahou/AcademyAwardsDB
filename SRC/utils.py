def getNumOrZeroIfNone(num):
    if num[0][0] is None:
        return 0
    else:
        return num[0][0]


def getQueryGenres(genres, withAnd=True, join_with="award.movie_id"):
    and_ = ""
    if withAnd:
        and_ = "AND"
    if len(genres) > 0:
        query_genre = f"{and_} {join_with} = movie_genre.movie_id AND ("
        for genre_id in genres:
            query_genre += f""" movie_genre.genre_id = {genre_id} OR """
        query_genre = query_genre[:-4] + ")\n"
        return query_genre
    return ""


def getQueryCategories(categories, withAnd=True):
    and_ = ""
    if withAnd:
        and_ = "AND"
    if len(categories) > 0:
        query_category = f"{and_} ("
        for category_id in categories:
            query_category += f"award.oscar_category_id = {category_id} OR "
        query_category = query_category[:-4] + ")\n"
        return query_category
    return ""


def getQueryAwardMinYear(min_year, withAnd=True):
    and_ = ""
    if withAnd:
        and_ = "AND"
    if min_year > 1934:
        return f" {and_} award.year >= %s\n" % min_year
    return ""


def getQueryAwardMaxYear(max_year, withAnd=True):
    and_ = ""
    if withAnd:
        and_ = "AND"
    if max_year < 2010:
        return f"{and_} award.year <= %s\n" % max_year
    return ""


def getQueryAwardWinner(only_winners, withAnd=True):
    and_ = ""
    if withAnd:
        and_ = "AND"
    if only_winners:
        return f"{and_} award.has_won = 1"
    return ""


def getHaving(withHaving):
    if withHaving:
        return "HAVING"
    return ""


def getFromGenre(is_exist):
    if is_exist:
        return """, movie_genre  """
    return ""


def getAwardAndMovieTable(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    genre_query = getQueryGenres(genres_list)
    tables = getAwardTable(min_year, max_year, only_winners, categories_list, genres_list)
    if len(genre_query) > 0:
        tables += ", movie "
    return tables


def getAwardTable(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    min_year_query = getQueryAwardMinYear(min_year)
    max_year_query = getQueryAwardMaxYear(max_year)
    category_query = getQueryCategories(categories_list)
    only_winners_query = getQueryAwardWinner(only_winners)
    genre_query = getQueryGenres(genres_list)
    sum_len = len(max_year_query + min_year_query + genre_query + category_query + only_winners_query)
    if sum_len > 0:
        return " , award "
    return ""



def getAwardPersonJoin(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    min_year_query = getQueryAwardMinYear(min_year)
    max_year_query = getQueryAwardMaxYear(max_year)
    category_query = getQueryCategories(categories_list)
    only_winners_query = getQueryAwardWinner(only_winners)
    genre_query = getQueryGenres(genres_list)
    sum_len = len(max_year_query + min_year_query + genre_query + category_query + only_winners_query)
    if sum_len > 0:
        return "AND award.id = award_person.award_id "
    return ""


def getAwardMovieJoin(genres_list=[]):

    genre_query = getQueryGenres(genres_list)
    sum_len = len(genre_query)
    if sum_len > 0:
        return "AND movie.id = award.movie_id "
    return ""

