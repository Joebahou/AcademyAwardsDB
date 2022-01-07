import create_db_script
import api_data_retrieve
import db_connector
import full_text_query
import oscar_query_2
import person
import person_queries
import retrieve_from_api
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import string
import movie_query
import create_db_indices

if __name__ == '__main__':

    # s_1 = 'the witcher gogo gaga'
    # s_2 = 'the witcher : gogo gaga'
    # unicode_line = s_2.translate({ord(c): None for c in '!@#$:'})
    # print(fuzz.ratio(s_1, s_2))
    # print(fuzz.ratio(s_1, unicode_line))
    try:
        db_connector.openConnection()

        # create_db_script.create_database_script()
        # person.checkPersonByDBID(3811,"Javier Bardem","f")
        # retrieve_from_api.retrieve_person()
        # create_db_script.create_database_script()
        # api_data_retrieve.retrieveMoviesAndPersonsFromCSV()
        # retrieve_from_api.addJobsToDB()
        # retrieve_from_api.retrieve_movies_and_cast()
        # retrieve_from_api.retrive_movie_imdb_id()
        # movie_query.num_of_wins_for_each_genre()
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
        #create_db_indices.create_indices()
        # full_text_query.feelingLuckyQuery("bi")
        # retrieve_from_api.helper()

    finally:
        db_connector.closeConnection()
