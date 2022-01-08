from SRC import db_connector


def feelingLuckyQuery(free_text):
    query = f"""  Select  title, original_language, popularity, release_date                        
                from    movie 
                where match (title) against ('{free_text}*' IN BOOLEAN MODE)
                order by popularity desc limit 10"""
    response = db_connector.getFromDB(query)
    for result in response:
        print(result)
    return response
