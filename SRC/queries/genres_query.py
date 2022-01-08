from SRC import db_connector


def num_of_noms_and_wins_for_each_genre():
    query = """ select numOfwins.genre,numOfnom.num_of_nominations,numOfwins.num_of_nominations
                FROM
                    (SELECT T.genre , count(*) AS num_of_nominations
                    FROM
                    (SELECT 
                        g.genre as genre, a.id as id, has_won
                    FROM
                        movie AS m,
                        award AS a,
                        genre AS g,
                        movie_genre AS m_g
                    WHERE
                            m.id = m_g.movie_id
                            AND m_g.genre_id = g.id
                            AND m.id = a.movie_id
                    GROUP BY g.id,a.id) as T
                    group by genre
                    order by num_of_nominations desc) numOfnom,
                    (select T.genre , count(*) AS num_of_nominations
                    from
                    (SELECT 
                        g.genre as genre, a.id as id, has_won
                    FROM
                        movie AS m,
                        award AS a,
                        genre AS g,
                        movie_genre AS m_g
                    WHERE
                            m.id = m_g.movie_id
                            AND m_g.genre_id = g.id
                            AND m.id = a.movie_id
                            and a.has_won=1
                    GROUP BY g.id,a.id) as T
                group by genre
                order by num_of_nominations desc) numOfwins
                where numOfwins.genre=numOfnom.genre """
    genres_count = db_connector.getFromDB(query)

    return genres_count
