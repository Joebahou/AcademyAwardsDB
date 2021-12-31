import create_db_script
import api_data_retrieve
import db_connector

if __name__ == '__main__':
    try:
        db_connector.openConnection()
        create_db_script.create_database_script()
        api_data_retrieve.retrieveMoviesAndPersonsFromCSV()
    finally:
        db_connector.closeConnection()
