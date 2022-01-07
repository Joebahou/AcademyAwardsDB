from SRC import db_connector

from SRC.queries import oscar_query_2
from SRC.queries import movie_query
from SRC.queries import person_queries
from SRC.queries import full_text_query

if __name__ == '__main__':
    try:
        db_connector.openConnection()
        ######## you can test here our queries ########

        movie_query.num_of_noms_and_wins_for_each_genre()
        print("************************************")
        oscar_query_2.getMovieWithMostAwards()
        print("************************************")
        oscar_query_2.getMovieWithMostNominations()
        print("************************************")
        oscar_query_2.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        print("************************************")
        oscar_query_2.getMovieAvgBudget(max_year=2000)
        print("************************************")
        oscar_query_2.getMovieMaxRevenue(genres_list=[12])
        print("************************************")
        oscar_query_2.getMovieAvgRevenue(categories_list=[22,21])
        print("************************************")
        oscar_query_2.getMovieMaxPopularity(only_winners=True)
        print("************************************")
        oscar_query_2.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        print("************************************")
        oscar_query_2.getPersonWithMostAwards(min_year=1980, genres_list=[12])
        print("************************************")
        oscar_query_2.getPersonWithMostNomi(min_year=1980)
        print("************************************")
        oscar_query_2.getPersonWithMostAwards(genres_list={12})
        print("************************************")
        oscar_query_2.getPersonWithMostNomi(genres_list={12}, categories_list=[22, 21])
        print("************************************")
        oscar_query_2.getPersonWithMostAwards(categories_list=[22, 21])
        print("************************************")
        oscar_query_2.getPersonWithMostNomi()
        print("************************************")
        movie_query.num_of_noms_and_wins_for_each_genre()
        oscar_query_2.getMovieWithMostAwards(max_year=2010, genres_list=[12])
        oscar_query_2.getPersonWithMostAwards(max_year=2010, genres_list=[12])
        oscar_query_2.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        oscar_query_2.getMovieAvgBudget(max_year=2010)
        oscar_query_2.getMovieMaxRevenue(max_year=2010)
        oscar_query_2.getMovieAvgRevenue(max_year=2010)
        oscar_query_2.getMovieMaxPopularity(max_year=2000, only_winners=True, genres_list={12})
        oscar_query_2.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        full_text_query.feelingLuckyQuery("bi")

    finally:
        db_connector.closeConnection()
