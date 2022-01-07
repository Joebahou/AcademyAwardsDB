import db_connector
import utils

COUNT_ALL = "count(*)"
BUDGET = "budget"
REVENUE = "revenue"
POPULARITY = "popularity"
MAX = "MAX({0})"
AVG = "AVG({0})"


def getMovieWithMostAwardsOrNominations(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", COUNT_ALL: "numOfAwards"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "numOfAwards", 5)
    response = db_connector.getFromDB(query)
    for result in response:
        print("title = ", str(result[0]), "numOfAwards = ", str(result[1]))
    return response


def getMovieWithMostAwards(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getMovieWithMostAwardsOrNominations(min_year, max_year, True, categories_list, genres_list)


def getMovieWithMostNominations(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getMovieWithMostAwardsOrNominations(min_year, max_year, False, categories_list, genres_list)


def getPersonWithMostAwardsOrMostNominations(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"person.name": "name", COUNT_ALL: "numOfAwards"}) + \
            getFromQuery(["person", "award_person"], len(genres_list) > 0) + \
            utils.getAwardTable(min_year, max_year, only_winners, categories_list, genres_list) + \
            getWhereQuery(min_year, max_year, only_winners, categories_list, genres_list, "person", "award_person") + \
            utils.getAwardPersonJoin(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("person.name", "numOfAwards", 5)
    response = db_connector.getFromDB(query)
    for result in response:
        print("title = ", str(result[0]), "numOfAwards = ", str(result[1]))

    return response


def getPersonWithMostAwards(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getPersonWithMostAwardsOrMostNominations(min_year, max_year, True, categories_list, genres_list)


def getPersonWithMostNomi(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getPersonWithMostAwardsOrMostNominations(min_year, max_year, False, categories_list, genres_list)


def getMovieMaxBudget(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", MAX.format(BUDGET): "maxBudget"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "maxBudget")
    response = db_connector.getFromDB(query)
    print("title = ", str(response[0][0]), "maxBudget = ", str(response[0][1]))
    return response


def getMovieAvgBudget(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(BUDGET): "avgBudget"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)
    print("avgBudget = ", str(response[0][0]))
    return response


def getMovieMaxRevenue(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", MAX.format(REVENUE): "maxRevenue"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "maxRevenue")
    response = db_connector.getFromDB(query)
    print("title = ", str(response[0][0]), "maxRevenue = ", str(response[0][1]))
    return response


def getMovieAvgRevenue(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(REVENUE): "avgRevenue"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)
    print("avgRevenue = ", str(response[0][0]))
    return response


def getMovieMaxPopularity(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", MAX.format(POPULARITY): "maxPopularity"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "maxPopularity")
    response = db_connector.getFromDB(query)
    print("title = ", str(response[0][0]), "maxPopularity = ", str(response[0][1]))
    return response


def getMovieAvgPopularity(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(POPULARITY): "avgPopularity"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)
    print("avgPopularity = ", str(response[0][0]))
    return response


def getSelectQuery(columns):
    select_query = "SELECT "

    for column in columns:
        select_query += f"{column} AS {columns[column]}, "
    return select_query[:-2]


def getFromQuery(tables, with_genres):
    from_query = " FROM "
    for table in tables:
        if len(table) > 0:
            from_query += f" {table} ,"
    from_query = from_query[:-2]
    return from_query + utils.getFromGenre(with_genres)


def getWhereQuery(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[],
                  nominee_table="movie", award_table="award"):
    min_year_query = utils.getQueryAwardMinYear(min_year)
    max_year_query = utils.getQueryAwardMaxYear(max_year)
    genre_query = utils.getQueryGenres(genres_list)
    category_query = utils.getQueryCategories(categories_list)
    only_winners_query = utils.getQueryAwardWinner(only_winners)
    where_query = f""" where {nominee_table}.id={award_table}.{nominee_table}_id {genre_query} {category_query} {min_year_query} {max_year_query} {only_winners_query} 
                 """
    return where_query


def getFromWhereQuery(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[],
                      nominee_table="movie", award_table="award"):
    from_query = getFromQuery({nominee_table, award_table}, len(genres_list) > 0)
    content = getWhereQuery(min_year, max_year, only_winners, categories_list, genres_list, nominee_table, award_table)
    return from_query + content


def getGroupOrderLimit(groupBy_col, order_col, limit=1):
    return f"group by {groupBy_col} order by {order_col} desc limit {limit}"
