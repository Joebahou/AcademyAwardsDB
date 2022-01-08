from SRC import db_connector
from SRC.API_DATA_RETRIEVE import retrieve_from_api
from SRC.API_DATA_RETRIEVE import csv_data_retrieve

from SRC.queries import oscar_query
from SRC.queries import movie_query
from SRC.queries import person_queries
from SRC.queries import full_text_query
from SRC.queries import genres_query
from SRC.CREATE_DB_SCRIPT import create_db_script
from SRC.CREATE_DB_SCRIPT import create_db_indices
from SRC.queries.movie_query import getMovieByName
from SRC.queries.oscar_query import getNominations, getMovieWithMostNominations
from SRC.queries.person_queries import getCountPersonWins, getCountPersonNominations, getCountPersonMovies

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

        #
        # print("************************************")
        # oscar_query.getMovieWithMostAwards()
        # print("************************************")
        # oscar_query.getMovieWithMostNominations()
        # print("************************************")
        # oscar_query.getMovieMaxBudget(max_year=2010, only_winners=True, genres_list=[12],categories_list=[22,21])
        # print("************************************")
        # oscar_query.getMovieAvgBudget(max_year=2000)
        # print("************************************")
        # oscar_query.getMovieMaxRevenue(genres_list=[12])
        # print("************************************")
        # oscar_query.getMovieAvgRevenue(categories_list=[22,21])
        # print("************************************")
        # oscar_query.getMovieMaxPopularity(only_winners=True)
        # print("************************************")
        # oscar_query.getMovieAvgPopularity(max_year=2000, only_winners=True, genres_list={12})
        # print("************************************")
        # oscar_query.getPersonWithMostAwards(min_year=1980, genres_list=[12])
        # print("************************************")
        # oscar_query.getPersonWithMostNomi(min_year=1980)
        # print("************************************")
        # oscar_query.getPersonWithMostAwards(genres_list={12})
        # print("************************************")
        # oscar_query.getPersonWithMostNomi(genres_list={12}, categories_list=[22, 21])
        # print("************************************")
        # oscar_query.getPersonWithMostAwards(categories_list=[22, 21])
        # print("************************************")
        # oscar_query.getPersonWithMostNomi()
        # print("************************************")
        # print(genres_query.num_of_noms_and_wins_for_each_genre())

        # print(oscar_query.getMovieMaxRevenue(max_year=2010))
        # print(oscar_query.getMovieMaxPopularity(max_year=2000, only_winners=True, genres_list={12}))

        # print(full_text_query.feelingLuckyQuery("bi"))
        # print(person_queries.getCountPersonMovies("Javier Bardem"))

        # print(getNominations(min_year=2010))
        # print(getNominations(only_winners=True, categories_list=[21, 22]))

        # print(getCountPersonMovies("Morgan Freeman"))
        # print(oscar_query.getMovieWithMostNominations(min_year=1990, max_year=2000, categories_list=[21, 22], genres_list=[12, 18]))

    finally:
        ######## closing connection to db ########

        db_connector.closeConnection()

        #################################################