######################## this is joe's file to work on api, do not delete ########################

import string

import mysql
import csv

from categories import *
import movie
import person
import categories
import job

api_key = "12d3cdb961e65887562f143725ee1a2b"

def retrieve_movies_and_cast():
    addJobsToDB()

    num_of_movies = movie.getMoviesCount()
    for i in range(num_of_movies):
        movie_ = movie.getMoviesByID(i)
        movie_title=movie_.title
        movie_sql_id=movie_.id



def addJobsToDB():
    job.insertJobByName("Acting")
    job.insertJobByName("Directing")
