import create_db_script
import mysql.connector
import api_data_retrieve

# connecting to localhost, later to our server.


# cnx = mysql.connector.connect(
#     host="mysqlsrv1.cs.tau.ac.il",
#     user="DbMysql34",
#     password="DbMysql34",
#     port=3306
# )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_db_script.create_database_script(cursor, DB_NAME)
    dataRetrieve = api_data_retrieve
    dataRetrieve.retrieveMoviesAndPersonsFromCSV()
    cursor.close()
    cnx.close()
