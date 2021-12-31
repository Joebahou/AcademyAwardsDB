######################## this is joe's file to work on api, do not delete ########################
import requests
import award
from categories import *
import movie
import person
import categories
import job

api_key = "12d3cdb961e65887562f143725ee1a2b"

def retrieve_movies_and_cast():


    num_of_movies = movie.getMoviesCount()
    start=movie.getLowestMovieID()
    movie_title=""
    for i in range(start,start+num_of_movies):
        movie_ = movie.getMoviesByID(i)
        movie_title=str(movie_.title)
        movie_title=movie_title.replace(" ","%20")
        movie_sql_id=movie_.id
        nomination_year=award.getMovieAwardYear(movie_sql_id)
        link= "https://api.themoviedb.org/3/search/movie?api_key="+api_key+ "&language=en-US&query="+movie_title +"&page=1&include_adult=true&year="+str(nomination_year)+"&primary_release_year="+str(nomination_year)
        response = requests.get(link)
        data = response.json()
        matched_in_db=False
        for d in data["results"]:
            if (d["title"]==movie_title) and (not matched_in_db):
                matched_in_db=True
                movie_db_id=d["id"]
                movie.updateMovie(movie_db_id)
            else:
                print("sql movie name = "+movie_title+" , db movie name = "+d["title"])
                continue
        if not matched_in_db:
            print("the movie "+ movie_title+"was not foind in api, please cheack why, not updating in sql, id= "+ str(i))





def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")







#no need for that now
def update_db():
    q="ALTER TABLE movie CHANGE COLUMN release_date release_date DATE NULL DEFAULT NULL "
    db_connector.insertToDB(q)
