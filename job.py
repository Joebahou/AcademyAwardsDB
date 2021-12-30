import db_connector


def insertJobByName(job):
    query = """INSERT INTO jobInMovie (job_name) VALUES (%s)""" % job
    return db_connector.insertToDB(query)

def getJobByName(job):
    query = """SELECT * FROM jobInMovie WHERE job_name = "%s" """ % job
    genres_from_db = db_connector.getFromDB(query)
    job=None
    for job_from_db in genres_from_db:
        job = Job(job_from_db[0],job_from_db[1])
    return job


class Job:
    def __init__(self, job_id, name):
        self.name = name
        self.genre_id = job_id
