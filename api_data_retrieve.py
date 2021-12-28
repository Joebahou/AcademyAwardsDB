import requests
import pandas as pd
import csv


def retrive_data_from_csv(cursor, cnx):
    categoriesForMovies = {1: "Animated Feature Film",
                           2: "Art Direction",
                           3: "Cinematography",
                           4: "Costume Design",
                           5: "Documentary (Feature)",
                           6: "Documentary (Short Subject)",
                           7: "Film Editing",
                           8: "Foreign Language Film",
                           9: "Makeup",
                           10: "Music (Scoring)",
                           11: "Music (Song)",
                           12: "Best Picture",
                           13: "Short Film (Animated)",
                           14: "Short Film (Live Action)",
                           15: "Sound",
                           16: "Sound Editing",
                           17: "Visual Effects",
                           18: "Writing",
                           19: "Writing"

                           }

    categoriesForPerson = { "Actor -- Leading Role",
                           "Actor -- Supporting Role",
                           "Actress -- Leading Role",
                           "Actress -- Supporting Role",
                           "Directing"

                           }

    file = open("Salary_Data.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    file.close()


def retrieve_data_for_db(cursor, cnx):
    api_key = "12d3cdb961e65887562f143725ee1a2b"
    link = "https://api.themoviedb.org/3/movie/144?api_key=12d3cdb961e65887562f143725ee1a2b&language=en-US"
    response = requests.get(link)
    tmp_link = "https://api.themoviedb.org/3/search/movie?api_key=12d3cdb961e65887562f143725ee1a2b&language=en-US&query=Toy%20Story%203&page=1&include_adult=false&year=2010&primary_release_year=2010"
    tmp_response = requests.get(tmp_link)
    d = tmp_response.json()

    datetmp = response.json()
    # getting first page
    data = response.json()

    # #appending pages 1 and 2
    # for i in range(1, 3):
    #     response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+api_key+"&language=en-US&page={}".format(i))
    #     temp_df = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]
    #     data.append(temp_df, ignore_index=False)

    add_movie = "INSERT INTO movies (movie_id,title) VALUES (%(movie_id)s,%(title)s)"

    row_dict = {
        'movie_id': 1,
        'title': data['title'],

    }
    cursor.execute(add_movie, row_dict)

    cnx.commit()

    # print(data.head())
