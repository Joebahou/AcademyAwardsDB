######################## this is joe's file to work on api, do not delete ########################
import requests
import award
from categories import *
import movie
import person
import categories
import job
from unidecode import unidecode
from fuzzywuzzy import fuzz
from datetime import datetime
from datetime import timedelta
import re

api_key = "12d3cdb961e65887562f143725ee1a2b"


def retrieve_person():
    num_of_person = person.getPersonCount()
    start = person.getLowestPersonID()
    for id in range(start, start + num_of_person):
        person_entry = person.getPersonByID(id)
        if not person_entry:
            continue
        person_name = person_entry.name
        person_name = person_name.strip()
        person_name_link = person_name.replace(" ", "%20")
        person_name = person_name.lower()
        person_link = "https://api.themoviedb.org/3/search/person?api_key=" + api_key + "&language=en-US&query=" + person_name_link + "&page=1&include_adult=true"
        response_person = requests.get(person_link)
        data_p = response_person.json()
        matched_in_db = False
        for d in data_p["results"]:
            n = d["name"].strip()
            n = n.lower()
            n = unidecode(n)
            if (fuzz.ratio(n, person_name) >= 90 and d["gender"] != 0):

                person_db_id = d["id"]
                person_gender = d["gender"]
                person.updatePerson(id, person_gender, person_db_id)
                matched_in_db = True
                break
            else:
                print("sql person name = " + person_name + " , db person name = " + n)

        if not matched_in_db:
            print("the person " + person_name + " was not found in api, please check why, not updating in sql, id= "
                  + str(id))


def retrive_movie_imdb_id():
    start = movie.getLowestMovieID()
    end = movie.getHighestMovieID()
    for i in range(start, end + 1):
        movie_ = movie.getMoviesByID(i)
        if not movie_:
            continue
        if movie_.release_date is None:
            continue
        db_id = movie_.db_id
        load_imdb(i, db_id)


def isSimilar(list_of_str1, list_of_str2):
    for s1 in list_of_str1:
        for s2 in list_of_str2:
            if fuzz.ratio(s1, s2) >= 90:
                return True
    return False


def fix_retrival():
    end = movie.getHighestMovieID()
    start = movie.getLowestMovieID()
    movie_title = ""
    movies = movie.getMoviesDateNull()
    for movie_ in movies:
        movie_title_db = str(movie_.title)
        movie_title = movie_title_db.replace("&", "and").split(" (")[0]
        movie_title_link = movie_title.replace(" ", "%20")
        # movie_title_link_between = re.search("\((.*?)\)", movie_title_link)
        # if not movie_title_link_between is None:
        #     movie_title_link = movie_title_link_between.group(1)
        movie_title = movie_title.lower().strip()
        # movie_title = movie_title.translate({ord(c): None for c in '!@#$:'})
        movie_sql_id = movie_.id
        nomination_year = award.getMovieAwardYear(movie_sql_id)
        link_for_movie = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + movie_title_link \
                         + "&page=1&include_adult=false"
        response_movie = requests.get(link_for_movie)
        data_movie = response_movie.json()
        matched_in_db = False
        movie_db_id = 0
        print("sql movie: " + movie_title + ", " + str(nomination_year))
        for d in data_movie["results"]:
            n = d["title"]
            n_original = d["original_title"].lower()
            n = n.strip()
            n = n.lower()
            n = unidecode(n)
            n = n.translate({ord(c): None for c in '!@#$:'})
            n_opt = n.replace("&", "and")
            n = n.translate({ord(c): None for c in '!@#$:'})
            sql_list = [movie_title, movie_title_db]
            all_movie_titles = movie_title.split("(")
            if len(all_movie_titles) > 1:
                sql_list.append(all_movie_titles[1])
            api_list = [n, n_opt, n_original]
            # if fuzz.ratio(movie_title, n) >= 90 or fuzz.ratio(movie_title_db, n) >= 90 or fuzz.ratio(movie_title,
            #                                                                                          n_opt) >= 90 \
            #         or fuzz.ratio(movie_title_db, n_opt) >= 90 or fuzz.ratio(movie_title, n_original) >= 90 \
            #         or fuzz.ratio(movie_title_db, n_original) >= 90:
            if isSimilar(sql_list, api_list):
                if len(d["release_date"]) > 0:
                    realese_date = datetime.strptime(d["release_date"], '%Y-%m-%d').year
                    if abs(nomination_year - realese_date) <= 2:
                        movie_db_id = d["id"]
                        movie.updateMovie(movie_sql_id, d["overview"], d["original_language"], d["popularity"],
                                          d["release_date"]
                                          , d["vote_average"], d["vote_count"], movie_db_id)
                        matched_in_db = True
                        break

            print("sql movie: " + movie_title + ", " + str(nomination_year) +
                  " \t, db movie: " + n + ", " + str(d["release_date"]))

        if not matched_in_db:
            print("the movie " + movie_title + " was not found in api, please check why, not updating in sql, id= "
                  + str(movie_sql_id) + "nomination year = " + str(nomination_year))

        else:
            load_more_details_on_movie(movie_sql_id, movie_db_id)
            load_cast_and_crew(movie_sql_id, movie_db_id)


def retrieve_movies_and_cast():
    end = movie.getHighestMovieID()
    start = movie.getLowestMovieID()
    movie_title = ""
    for i in range(start, end + 1):
        movie_ = movie.getMoviesByID(i)
        if not movie_:
            continue
        if movie_.release_date is not None:
            continue
        movie_title_db = str(movie_.title)
        movie_title = movie_title_db.replace("&", "and")
        if "(" in movie_title:
            movie_title_brack = movie_title.split('(', 1)[1].split(')')[0]
            if movie_title_brack:
                movie_title = movie_title.replace("(" + movie_title_brack + ")", "")
        movie_title_link = movie_title.replace(" ", "%20")
        movie_title = movie_title.lower().strip()
        movie_title = movie_title.translate({ord(c): None for c in '!@#$:'})
        movie_sql_id = movie_.id
        nomination_year = award.getMovieAwardYear(movie_sql_id)
        link_for_movie = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + movie_title_link \
                         + "&page=1&include_adult=false&year=" + str(nomination_year)
        response_movie = requests.get(link_for_movie)
        data_movie = response_movie.json()
        matched_in_db = False
        movie_db_id = 0
        for d in data_movie["results"]:
            n = d["title"]
            n_original = d["original_title"]
            n = n.strip()
            n = n.lower()
            n = unidecode(n)
            n = n.translate({ord(c): None for c in '!@#$:'})
            n_opt = n.replace("&", "and")
            n = n.translate({ord(c): None for c in '!@#$:'})
            if (fuzz.ratio(movie_title, n) >= 70 or fuzz.ratio(movie_title_db, n) >= 70 or fuzz.ratio(movie_title,
                                                                                                      n_opt) >= 70 or \
                fuzz.ratio(movie_title_db, n_opt) >= 70 or n.find(movie_title) or movie_title.find(n) or \
                n_opt.find(movie_title) or movie_title.find(n_opt)) or fuzz.ratio(movie_title, n_original) >= 70 \
                    or fuzz.ratio(movie_title_db, n_original) >= 70 or n_original.find(movie_title) or movie_title.find(
                n_original):

                movie_db_id = d["id"]
                movie.updateMovie(i, d["overview"], d["original_language"], d["popularity"], d["release_date"]
                                  , d["vote_average"], d["vote_count"], movie_db_id)
                matched_in_db = True
                break
            else:
                print("sql movie name = " + movie_title + " , db movie name = " + n)

        if not matched_in_db:
            print("the movie " + movie_title + " was not found in api, please check why, not updating in sql, id= "
                  + str(i) + "nomination year = " + str(nomination_year))

        else:
            load_more_details_on_movie(i, movie_db_id)
            load_cast_and_crew(i, movie_db_id)


def load_cast_and_crew(movie_id, movie_db_id):
    link_for_crew_and_cast = "https://api.themoviedb.org/3/movie/" + str(
        movie_db_id) + "/credits?api_key=" + api_key + "&language=en-US"
    response_crew = requests.get(link_for_crew_and_cast)
    data = response_crew.json()
    person.load_cast_and_crew(movie_id, data["cast"], data["crew"])


def load_more_details_on_movie(movie_id, movie_db_id):
    link = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "?api_key=" + api_key + "&language=en-US"
    response = requests.get(link)
    data = response.json()
    movie.insert_revenue_genres_company_prod(movie_id, data["budget"], data["revenue"], data["genres"],
                                             data["production_companies"], movie_db_id)


def load_imdb(movie_id, movie_db_id):
    link = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "?api_key=" + api_key + "&language=en-US"
    response = requests.get(link)
    data = response.json()
    movie.insert_imdb(movie_id, data["imdb_id"])


def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")


def helper():
    title = "The Emigrants"
    title = title.replace(" ", "%20")
    link_for_movie = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&" \
                                                                                      "query=" + title + "&page=1&include_adult=true"
    response = requests.get(link_for_movie)
    data = response.json()
    d = data["results"]
    n = d[0]["title"].strip()
    n = unidecode(n)
    print(n)


def helperApi():
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"r": "json", "i": "tt1164999"}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "47ee3eacacmsh97e81151536051ep194a32jsn93131f716ddf"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# no need for that now
def update_db():
    q = "ALTER TABLE movie CHANGE COLUMN release_date release_date DATE NULL DEFAULT NULL "
    db_connector.insertToDB(q)
