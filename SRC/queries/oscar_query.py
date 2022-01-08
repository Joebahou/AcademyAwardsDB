from SRC import db_connector
from SRC import utils

COUNT_ALL = "count(*)"
BUDGET = "budget"
REVENUE = "revenue"
POPULARITY = "popularity"
MAX = "MAX({0})"
AVG = "AVG({0})"


def getNominations(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    min_year_query = utils.getQueryAwardMinYear(min_year, False)
    with_and = len(min_year_query) > 0
    max_year_query = utils.getQueryAwardMaxYear(max_year, with_and)
    with_and = len(min_year_query + max_year_query) > 0
    only_winners_query = utils.getQueryAwardWinner(only_winners, with_and)
    with_and = len(min_year_query + max_year_query + only_winners_query) > 0
    category_query = utils.getQueryCategories(categories_list, with_and)
    with_having = len(min_year_query + max_year_query + only_winners_query + category_query)
    having = utils.getHaving(with_having)
    genre_from = utils.getFromGenre(len(genres_list))
    genre_query = utils.getQueryGenres(genres_list, join_with="movie.id")
    query = f"""SELECT 	awardJoinPerson.awardYear, 
		        oscarCategory.category, 
                movie.title,
                awardJoinPerson.personName,
                awardJoinPerson.won
                FROM movie, oscarCategory {genre_from},
	                (SELECT person.name as personName,
			                award.id as awardId, award.year as awardYear, award.oscar_category_id as categoryId,
			                award.movie_id as mivieId, award.has_won as won
	                From award_person
	                right join award on award.id = award_person.award_id
	                left join person on person.id = award_person.person_id
	            {having} {min_year_query} {max_year_query} {only_winners_query} {category_query}) as awardJoinPerson
                WHERE oscarCategory.id = awardJoinPerson.categoryId
                AND movie.id = awardJoinPerson.mivieId
                 {genre_query}
                order by awardJoinPerson.awardYear desc, oscarCategory.category, awardJoinPerson.won desc
"""
    response = db_connector.getFromDB(query)
    return response


def getMovieWithMostAwardsOrNominations(min_year=1934, max_year=2010, only_winners=False, categories_list=[],
                                        genres_list=[]):
    query = getSelectQuery({"title": "title", COUNT_ALL: "numOfAwards"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "numOfAwards", 5)
    response = db_connector.getFromDB(query)
    return response


def getMovieWithMostAwards(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getMovieWithMostAwardsOrNominations(min_year, max_year, True, categories_list, genres_list)


def getMovieWithMostNominations(min_year=1934, max_year=2010, categories_list=[], genres_list=[]):
    return getMovieWithMostAwardsOrNominations(min_year, max_year, False, categories_list, genres_list)


def getPersonWithMostAwardsOrMostNominations(min_year=1934, max_year=2010, only_winners=False, categories_list=[],
                                             genres_list=[]):
    query = getSelectQuery({"person.name": "name", COUNT_ALL: "numOfAwards"}) + \
            getFromQuery(["person", "award_person"], len(genres_list) > 0) + \
            utils.getAwardTable(min_year, max_year, only_winners, categories_list, genres_list) + \
            getWhereQuery(min_year, max_year, only_winners, categories_list, genres_list, "person", "award_person") + \
            utils.getAwardPersonJoin(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("person.name", "numOfAwards", 5)
    response = db_connector.getFromDB(query)

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
    return response


def getMovieAvgBudget(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(BUDGET): "avgBudget"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)

    return response


def getMovieMaxRevenue(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", MAX.format(REVENUE): "maxRevenue"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "maxRevenue")
    response = db_connector.getFromDB(query)

    return response


def getMovieAvgRevenue(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(REVENUE): "avgRevenue"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)

    return response


def getMovieMaxPopularity(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({"title": "title", MAX.format(POPULARITY): "maxPopularity"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list) + \
            getGroupOrderLimit("title", "maxPopularity")
    response = db_connector.getFromDB(query)

    return response


def getMovieAvgPopularity(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    query = getSelectQuery({AVG.format(POPULARITY): "avgPopularity"}) + \
            getFromWhereQuery(min_year, max_year, only_winners, categories_list, genres_list)
    response = db_connector.getFromDB(query)

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
    where_query = f""" WHERE {nominee_table}.id={award_table}.{nominee_table}_id {genre_query} {category_query} {min_year_query} {max_year_query} {only_winners_query} 
                 """
    return where_query


def getFromWhereQuery(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[],
                      nominee_table="movie", award_table="award"):
    from_query = getFromQuery({nominee_table, award_table}, len(genres_list) > 0)
    content = getWhereQuery(min_year, max_year, only_winners, categories_list, genres_list, nominee_table, award_table)
    return from_query + content


def getGroupOrderLimit(groupBy_col, order_col, limit=1):
    return f"group by {groupBy_col} order by {order_col} desc limit {limit}"
