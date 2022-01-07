import db_connector



def feelingLuckyQuery(free_text):
    query=f"""Select * from movie where match (title) against ('{free_text}*' IN BOOLEAN MODE) limit 25"""
    response=db_connector.getFromDB(query)
    for result in response:
        print("title = ", result[1], )
        print("Budget = ", result[2])
        print("Overview  = ", result[3])
        print("Original language = ", result[4])
        print("Popularity  = ", result[5])
        print("Release date  = ", result[6])
        print("Revenue  = ", result[7])
        print("Vote average  = ", result[8])
        print("Vote count   = ", result[9], "\n")