from SRC import db_connector

from SRC.CREATE_DB_SCRIPT import create_db_script
from SRC.CREATE_DB_SCRIPT import create_db_indices

if __name__ == '__main__':
    try:
        db_connector.openConnection()
        # create_db_script.create_database_script()
        # create_db_indices.create_indices()

    finally:
        db_connector.closeConnection()
