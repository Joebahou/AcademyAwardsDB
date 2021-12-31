import create_db_script
import api_data_retrieve
import db_connector
import retrieve_from_api

if __name__ == '__main__':
    try:
        db_connector.openConnection()

        # create_db_script.create_database_script()
        # api_data_retrieve.retrieveMoviesAndPersonsFromCSV()
        # retrieve_from_api.addJobsToDB()
        retrieve_from_api.retrieve_movies_and_cast()
    finally:
        db_connector.closeConnection()
