import requests
import pandas as pd
# udis key = 7136f4075d33998d3d77a11a9c442439

def retrieve_data_for_db(cursor,cnx):
    api_key = "XXXXXXXXXXXXXXXXXXXX"
    link = "https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_key + "&language=en-US&page=1"
    response = requests.get(link)

    response.json()["results"]

    #getting first page
    data = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]

    #appending pages 1 and 2
    for i in range(1, 3):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+api_key+"&language=en-US&page={}".format(i))
        temp_df = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]
        data.append(temp_df, ignore_index=False)


    add_movie=("INSERT INTO movies (movie_id,title,vote_average) VALUES (%(movie_id)s,%(title)s,%(vote_average)s)")

    for index, row in data.iterrows():
      row_dict = {
        'movie_id':row['id'],
        'title':row['title'],
        'vote_average':row['vote_average']
      }
      cursor.execute(add_movie, row_dict)

    cnx.commit()

    print(data.head())
