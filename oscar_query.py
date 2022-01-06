import db_connector


def getMovieMaxBudget(min_year,max_year,only_winners=False,categories_list=[]):
    category_query=""
    if len(categories_list)>0:
        category_query="AND c"