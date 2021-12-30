import mysql.connector
from mysql.connector import errorcode


# function which creates the DB
def create_database(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# actually creating the DB
def create_database_script(cursor, DB_NAME):
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            print("Database {} created successfully.".format(DB_NAME))

        else:
            print("err")
            exit(1)

    TABLES = {}
    TABLES['movie'] = ("CREATE TABLE movie (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,title VARCHAR(150),"
                       "budget INT,overview VARCHAR(500),original_language CHAR(45),"
                       "popularity INT,release_date VARCHAR(45),revenue INT,"
                       "vote_average FLOAT,vote_count INT, db_id INT)")

    TABLES['genre'] = "CREATE TABLE genre (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, genre VARCHAR(45))"

    TABLES['movie_genre'] = ("CREATE TABLE movie_genre (movie_id INT NOT NULL, genre_id INT NOT NULL, PRIMARY KEY"
                             " (movie_id, genre_id), FOREIGN KEY (movie_id) REFERENCES movie(id), FOREIGN KEY "
                             "(genre_id) REFERENCES genre(id))")

    TABLES['person'] = ("CREATE TABLE person (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(45),gender INT,"
                        "original_name VARCHAR(45), db_id INT )")

    TABLES['jobInMovie'] = "CREATE TABLE jobInMovie(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,job_name VARCHAR(45))"

    TABLES['person_movie_job'] = (
        "CREATE TABLE person_movie_job (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,person_id INT NOT"
        " NULL,movie_id INT NOT NULL,job_id INT NOT NULL,FOREIGN KEY (movie_id) REFERENCES"
        " movie(id) , FOREIGN KEY (person_id) REFERENCES person(id),"
        "FOREIGN KEY (job_id) REFERENCES jobInMovie(id))")

    TABLES['oscarCategory'] = "CREATE TABLE oscarCategory (id INT NOT NULL PRIMARY KEY,category VARCHAR(45))"

    TABLES['award'] = (
        "CREATE TABLE award (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,year INT NOT NULL,oscar_category_id INT NOT NULL"
        ",movie_id INT NOT NULL,has_won BIT,FOREIGN KEY (oscar_category_id) REFERENCES oscarCategory(id),"
        "FOREIGN KEY (movie_id) REFERENCES movie(id))")

    TABLES['award_person'] = ("CREATE TABLE award_person (award_id INT NOT NULL PRIMARY KEY,person_id INT NOT NULL,"
                              "FOREIGN KEY (person_id) REFERENCES person(id),FOREIGN KEY (award_id) REFERENCES "
                              "award(id) )")

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
