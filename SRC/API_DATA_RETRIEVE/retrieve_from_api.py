
import requests
from . import award
from . import movie
from . import person
from . import job
from unidecode import unidecode
from fuzzywuzzy import fuzz
from datetime import datetime


api_key = "12d3cdb961e65887562f143725ee1a2b"
# udis key = 7136f4075d33998d3d77a11a9c442439


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





def isSimilar(list_of_str1, list_of_str2):
    for s1 in list_of_str1:
        for s2 in list_of_str2:
            if fuzz.ratio(s1, s2) >= 90:
                return True
    return False


def load_new_details_on_movie(movie_id, movie_db_id):
    link = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "?api_key=" + api_key + "&language=en-US"
    response = requests.get(link)
    data = response.json()
    movie.update_revenue_genres_company_prod(movie_id, data["budget"], data["revenue"], data["genres"],
                                             data["production_companies"], movie_db_id)


    

def retrieveSecondTry():
    end = movie.getHighestMovieID()
    start = movie.getLowestMovieID()
    movie_title = ""
    movies = movie.getMoviesDateNull()
    for movie_ in movies:
        movie_title_db = str(movie_.title)
        movie_title = movie_title_db.replace("&", "and").split(" (")[0]
        movie_title_link = movie_title.replace(" ", "%20")
        movie_title = movie_title.lower().strip()
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

                if len(d["release_date"]) > 0:
                    realese_date = datetime.strptime(d["release_date"], '%Y-%m-%d').year
                    if abs(nomination_year - realese_date) <= 2:
                        movie_db_id = d["id"]
                        movie.updateMovie(movie_sql_id, d["overview"], d["original_language"], d["popularity"],
                                          d["release_date"]
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

def load_new_cast_and_crew(movie_id, movie_db_id):
        link_for_crew_and_cast = "https://api.themoviedb.org/3/movie/" + str(
            movie_db_id) + "/credits?api_key=" + api_key + "&language=en-US"
        response_crew = requests.get(link_for_crew_and_cast)
        data = response_crew.json()
        person.load_new_cast_and_crew(movie_id, data["cast"], data["crew"])


def load_more_details_on_movie(movie_id, movie_db_id):
    link = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "?api_key=" + api_key + "&language=en-US"
    response = requests.get(link)
    data = response.json()
    movie.insert_revenue_genres_company_prod(movie_id, data["budget"], data["revenue"], data["genres"],
                                             data["production_companies"], movie_db_id)





def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")





