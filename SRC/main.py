from SRC import db_connector
from SRC.API_DATA_RETRIEVE import retrieve_from_api
from SRC.API_DATA_RETRIEVE import csv_data_retrieve

from SRC.queries import oscar_query_2
from SRC.queries import movie_query
from SRC.queries import person_queries
from SRC.queries import full_text_query
from SRC.queries import genres_query
from SRC.CREATE_DB_SCRIPT import create_db_script
from SRC.CREATE_DB_SCRIPT import create_db_indices


if __name__ == '__main__':
    try:

        ######## opening connection to db ########

        db_connector.openConnection()

        #################################################

        ######## creating db ########
        # create_db_script.create_database_script()
        # create_db_indices.create_indices()
        #################################################

        ######## data retrieve ########

        # csv_data_retrieve.retrieveFromCSV()
        # retrieve_from_api.addJobsToDB()
        # retrieve_from_api.retrieve_person()
        # retrieve_from_api.retrieve_movies_and_cast()
        # retrieve_from_api.retrieveSecondTry()

        #################################################

        ######## creating indices ########

        # create_db_indices.create_indices()

        #################################################

        ######## queries ########

        ######## you can test here our queries ########
        ######## explaination for each method is in the software-docs ########


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
        genres_query.num_of_noms_and_wins_for_each_genre()
        oscar_query_2.getMovieWithMostAwards(max_year=2010, genres_list=[12])
        oscar_query_2.getPersonWithMostAwards(max_year=2010, genres_list=[12])
        oscar_query_2.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        oscar_query_2.getMovieAvgBudget(max_year=2010)
        oscar_query_2.getMovieMaxRevenue(max_year=2010)
        oscar_query_2.getMovieAvgRevenue(max_year=2010)
        oscar_query_2.getMovieMaxPopularity(max_year=2000, only_winners=True, genres_list={12})
        oscar_query_2.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        full_text_query.feelingLuckyQuery("bi")
        person_queries.getCountPersonMovies("Javier Bardem")


    finally:
        ######## closing connection to db ########

        db_connector.closeConnection()

        #################################################