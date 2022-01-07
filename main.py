import SRC.CREATE_DB_SCRIPT.create_db_indices
import SRC.queries.full_text_query
import SRC.queries.movie_query
import SRC.queries.oscar_query_2
from SRC import db_connector
from SRC.API_DATA_RETRIEVE import retrieve_from_api, csv_data_retrieve
from SRC.CREATE_DB_SCRIPT import create_db_script, create_db_indices
from SRC.queries import movie_query, oscar_query_2, full_text_query

if __name__ == '__main__':

    try:
        db_connector.openConnection()

        # create_db_script.create_database_script()
        #
        # retrieve_from_api.retrieve_person()
        # create_db_script.create_database_script()
        # api_data_retrieve.retrieveMoviesAndPersonsFromCSV()
        # retrieve_from_api.addJobsToDB()
        # retrieve_from_api.retrieve_movies_and_cast()
        # retrieve_from_api.retrive_movie_imdb_id()
        # movie_query.num_of_noms_and_wins_for_each_genre()
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieWithMostAwards()
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieWithMostNominations()
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieAvgBudget(max_year=2000)
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieMaxRevenue(genres_list=[12])
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieAvgRevenue(categories_list=[22,21])
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieMaxPopularity(only_winners=True)
        # print("************************************")
        # SRC.queries.oscar_query_2.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostAwards(min_year=1980, genres_list=[12])
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostNomi(min_year=1980)
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostAwards(genres_list={12})
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostNomi(genres_list={12}, categories_list=[22, 21])
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostAwards(categories_list=[22, 21])
        # print("************************************")
        # SRC.queries.oscar_query_2.getPersonWithMostNomi()
        # print("************************************")
        # SRC.queries.movie_query.num_of_noms_and_wins_for_each_genre()
        # oscar_query_2.getMovieWithMostAwards(max_year=2010, genres_list=[12])
        # oscar_query_2.getPersonWithMostAwards(max_year=2010, only_winners=True, genres_list=[12])
        # oscar_query_2.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        # oscar_query_2.getMovieAvgBudget(max_year=2010)
        # oscar_query_2.getMovieMaxRevenue(max_year=2010)
        # oscar_query_2.getMovieAvgRevenue(max_year=2010)
        # oscar_query_2.getMovieMaxPopularity(max_year=2000, only_winners=True, genres_list={12})
        # oscar_query_2.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        # create_db_indices.create_indices()
        full_text_query.feelingLuckyQuery("bi")


    finally:
        db_connector.closeConnection()
