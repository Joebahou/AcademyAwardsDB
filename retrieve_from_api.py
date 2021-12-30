######################## this is joe's file to work on api, do not delete ########################

import string

import mysql
import csv

from categories import *
import movie
import person
import categories


def retrieve_movies_and_cast():
    addGenresToDB()

    num_of_movies=movie.getMoviesCount()
    for i in range(num_of_movies):
        movie_=movie.getMoviesByID(i)
        movie_.title


def addGenresToDB():
    pass