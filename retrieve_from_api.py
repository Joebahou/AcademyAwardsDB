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

api_key = "12d3cdb961e65887562f143725ee1a2b"

def retrieve_person():
    num_of_person = person.getPersonCount()
    start= person.getLowestPersonID()
    for id in range(start,start+num_of_person):
        person_entry= person.getPersonByID(id)
        if not person_entry:
            continue
        person_name=person_entry.name
        person_name = person_name.strip()
        person_name_link=person_name.replace(" ","%20")
        person_name = person_name.lower()
        person_link="https://api.themoviedb.org/3/search/person?api_key="+api_key +"&language=en-US&query="+person_name_link+"&page=1&include_adult=true"
        response_person = requests.get(person_link)
        data_p=response_person.json()
        matched_in_db = False
        for d in data_p["results"]:
            n=d["name"].strip()
            n= n.lower()
            n=unidecode(n)
            if (fuzz.ratio(n, person_name) >= 90 and d["gender"]!=0):

                person_db_id = d["id"]
                person_gender=d["gender"]
                person.updatePerson(id,person_gender,person_db_id)
                matched_in_db = True
                break
            else:
                print("sql person name = " + person_name + " , db person name = " + n)

        if not matched_in_db:
            print("the person " + person_name + " was not found in api, please check why, not updating in sql, id= "
                  + str(id))


def retrieve_movies_and_cast():
    num_of_movies = movie.getMoviesCount()
    start=movie.getLowestMovieID()
    movie_title=""
    for i in range(start,start+num_of_movies):
        movie_ = movie.getMoviesByID(i)
        movie_title_db=str(movie_.title)
        movie_title=movie_title_db.replace("&","and")

        movie_title_link=movie_title.replace(" ","%20")
        movie_title = movie_title.lower().strip()
        movie_title = movie_title.translate({ord(c): None for c in '!@#$:'})
        movie_sql_id=movie_.id
        nomination_year=award.getMovieAwardYear(movie_sql_id)
        link_for_movie= "https://api.themoviedb.org/3/search/movie?api_key="+api_key+ "&language=en-US&query="+movie_title_link \
              +"&page=1&include_adult=false&year="+str(nomination_year)+"&primary_release_year="+str(nomination_year)
        response_movie = requests.get(link_for_movie)
        data_movie = response_movie.json()
        matched_in_db = False
        movie_db_id = 0
        for d in data_movie["results"]:
            n=d["title"]
            n=n.strip()
            n=n.lower()
            n=unidecode(n)
            n = n.translate({ord(c): None for c in '!@#$:'})
            if (fuzz.ratio(movie_title,n)>=90 or fuzz.ratio(movie_title_db,n)>=90) :
                movie_db_id=d["id"]

                movie.updateMovie(i,d["overview"],d["original_language"],d["popularity"],d["release_date"]
                                  ,d["vote_average"],d["vote_count"],movie_db_id)
                matched_in_db = True
                break
            else:
                print("sql movie name = "+movie_title+" , db movie name = "+n)

        if not matched_in_db:
            print("the movie "+ movie_title+" was not found in api, please check why, not updating in sql, id= "
                  + str(i)+"nomination year = "+ str(nomination_year))

        else:
            load_more_details_on_movie(i,movie_db_id)
            load_cast_and_crew(i,movie_db_id)




def load_cast_and_crew(movie_id,movie_db_id):
    link_for_crew_and_cast = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "/credits?api_key=" + api_key + "&language=en-US"
    response_crew = requests.get(link_for_crew_and_cast)
    data = response_crew.json()
    person.load_cast_and_crew(movie_id,data["cast"],data["crew"])

def load_more_details_on_movie(movie_id,movie_db_id):
    link = "https://api.themoviedb.org/3/movie/" + str(movie_db_id) + "?api_key=" + api_key + "&language=en-US"
    response= requests.get(link)
    data = response.json()
    movie.insert_revenue_genres_company_prod(movie_id,data["budget"],data["revenue"],data["genres"],movie_db_id)


def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")



def helper():
    person_link = "https://api.themoviedb.org/3/search/person?api_key=" + api_key + "&language=en-US&query=Grace%20Moore&page=1&include_adult=true"
    response = requests.get(person_link)
    data = response.json()
    d=data["results"]
    n=d[0]["title"].strip()
    n=unidecode(n)
    print(n)



#no need for that now
def update_db():
    q="ALTER TABLE movie CHANGE COLUMN release_date release_date DATE NULL DEFAULT NULL "
    db_connector.insertToDB(q)
