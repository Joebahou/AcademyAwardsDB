import db_connector
import utils


def getFromGenre(is_exist):
    if is_exist:
        return """, genre , movie_genre  """
    return ""


def getMovieMaxBudget(min_year=1934, max_year=2010, only_winners=False, categories_list=[], genres_list=[]):
    min_year_query = utils.getQueryAwardMinYear(min_year)
    max_year_query = utils.getQueryAwardMaxYear(max_year)
    genre_query = utils.getQueryGenres(genres_list)
    category_query = utils.getQueryCategories(categories_list)
    only_winners_query = utils.getQueryAwardWinner(only_winners)
    select_query = """ SELECT title, Max(budget) as maxBudget """
    from_query = """ From movie , award """
    from_query += getFromGenre(len(genres_list) > 0)
    content = f"""where movie.id=award.movie_id {genre_query}  {category_query}  {min_year_query}  {max_year_query} 
    {only_winners_query} 
    group by title 
    order by maxBudget desc 
    limit 1 """

    query = select_query + from_query + content
    max_budget = db_connector.getFromDB(query)
    print("title = ", str(max_budget[0][0]), "budget = ", str(max_budget[0][1]))
