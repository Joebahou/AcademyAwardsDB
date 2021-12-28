import create_db_script
import mysql.connector
import api_data_retrieve

# connecting to localhost, later to our server.
cnx = mysql.connector.connect(
  host="localhost",
  user="DbMysql34",
  password="DbMysql34",
  port=3305
)

DB_NAME = 'DbMysql34'

cnx.database = DB_NAME

cursor = cnx.cursor()







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create_db_script.create_database_script(cursor,DB_NAME)
    api_data_retrieve.retrieve_data_for_db(cursor,cnx)
    cursor.close()
    cnx.close()

