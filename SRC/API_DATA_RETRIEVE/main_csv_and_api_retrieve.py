from SRC import db_connector

from SRC.API_DATA_RETRIEVE import retrieve_from_api
from SRC.API_DATA_RETRIEVE import csv_data_retrieve

if __name__ == '__main__':
    try:
        db_connector.openConnection()
        # csv_data_retrieve.retrieveFromCSV()
        # retrieve_from_api.addJobsToDB()
        # retrieve_from_api.retrieve_person()
        # retrieve_from_api.retrieve_movies_and_cast()
        # retrieve_from_api.retrieveSecondTry()


    finally:
        db_connector.closeConnection()
