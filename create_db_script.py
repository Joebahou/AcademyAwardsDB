import mysql.connector
from mysql.connector import errorcode

# function which creates the DB
def create_database(cursor,DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# actually creating the DB
def create_database_script(cursor,DB_NAME):
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor,DB_NAME)
            print("Database {} created successfully.".format(DB_NAME))

        else:
            print("err")
            exit(1)


    TABLES = {}
    TABLES['movies'] = ("CREATE TABLE movies (movie_id INT NOT NULL PRIMARY KEY,title VARCHAR(250),adult BOOL,"
                        "budget INT,imdb_id VARCHAR(250),overview VARCHAR(1000),original_language CHAR(250),"
                        "popularity INT,release_date VARCHAR(250),revenue INT,status VARCHAR(250),"
                        "vote_average FLOAT,vote_count INT,video VARCHAR(250))")
    TABLES['genres']=("CREATE TABLE genres (genre_id INT NOT NULL PRIMARY KEY, genre VARCHAR(250))")



    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
