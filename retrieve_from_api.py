######################## this is joe's file to work on api, do not delete ########################

import string

import mysql
import csv

import award
from categories import *
import movie
import person
import categories
import job

api_key = "12d3cdb961e65887562f143725ee1a2b"

def retrieve_movies_and_cast():
    addJobsToDB()

    num_of_movies = movie.getMoviesCount()
    movie_title=""
    for i in range(num_of_movies):
        movie_ = movie.getMoviesByID(i)
        movie_title=str(movie_.title)
        movie_title=movie_title.replace(" ","%20")
        movie_sql_id=movie_.id
        nomination_year=award.getMovieAwardYear(movie_sql_id)
        link= "https://api.themoviedb.org/3/search/movie?api_key="+api_key+ "&language=en-US&query="+movie_title +"&page=1&include_adult=true&year="+nomination_year+"&primary_release_year="+nomination_year



def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")
