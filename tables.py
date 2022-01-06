TABLES = {}
TABLES['movie'] = ("CREATE TABLE movie (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,title VARCHAR(150),"
                   "budget INT(16),overview VARCHAR(1000),original_language CHAR(45),"
                   "popularity INT,release_date DATE,revenue INT(16),"
                   "vote_average FLOAT,vote_count INT, db_id INT,imdb_id CHAR(50) )")

TABLES['genre'] = "CREATE TABLE genre (id INT NOT NULL PRIMARY KEY , genre VARCHAR(45))"

TABLES['movie_genre'] = ("CREATE TABLE movie_genre (movie_id INT NOT NULL, genre_id INT NOT NULL, PRIMARY KEY"
                         " (movie_id, genre_id), FOREIGN KEY (movie_id) REFERENCES movie(id), FOREIGN KEY "
                         "(genre_id) REFERENCES genre(id))")

TABLES['person'] = ("CREATE TABLE person (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,name VARCHAR(45),gender INT,"
                    "db_id INT )")

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

TABLES['award_person'] = ("CREATE TABLE award_person (award_id INT NOT NULL,person_id INT NOT NULL,"
                          "FOREIGN KEY (person_id) REFERENCES person(id),FOREIGN KEY (award_id) REFERENCES "
                          "award(id),PRIMARY KEY (award_id,person_id))")

TABLES['production_company']="CREATE TABLE production_company (id INT NOT NULL PRIMARY KEY , name VARCHAR(100))"


TABLES['movie_production_company'] = ("CREATE TABLE movie_production_company (movie_id INT NOT NULL, production_company_id INT NOT NULL, PRIMARY KEY"
                         " (movie_id, production_company_id), FOREIGN KEY (movie_id) REFERENCES movie(id), FOREIGN KEY "
                         "(production_company_id) REFERENCES production_company(id))")