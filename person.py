from unidecode import unidecode

import db_connector
import utils
from utils import getNumOrZeroIfNone


def isPersonExistsInDB(personName):
    persons = getPersonsByName(personName)
    return len(persons) > 0


def getPersonsByName(personName):
    query = """SELECT * FROM person WHERE name = "%s" """ % personName
    persons_from_db = db_connector.getFromDB(query)
    persons = []
    for person_from_db in persons_from_db:
        person = Person(person_from_db[0],
                        person_from_db[1],
                        person_from_db[2],
                        person_from_db[3])
        persons.append(person)
    return persons


def getHighestPersonID():
    query = """SELECT MAX(id) FROM person"""
    highest_id = db_connector.getFromDB(query, 1)
    return getNumOrZeroIfNone(highest_id)


def getLowestPersonID():
    query = """SELECT MIN(id) FROM person"""
    highest_id = db_connector.getFromDB(query)
    return utils.getNumOrZeroIfNone(highest_id)


def getPersonCount():
    query = ("SELECT COUNT(*) FROM person")
    return db_connector.getFromDB(query, 1)[0][0]


def getPersonByID(id_):
    query = """SELECT * FROM person WHERE id = %s """ % id_
    persons_from_db = db_connector.getFromDB(query, 1)
    person = None
    for person_from_db in persons_from_db:
        person = Person(person_from_db[0], person_from_db[1], person_from_db[2], person_from_db[3])

    return person


def checkPersonByDBID(db_id, name, original_name):
    query = ("SELECT id FROM person WHERE (name=%s and  db_id =%s) or (name=%s and  db_id =%s)")
    val = (name, db_id, original_name, db_id)
    id = db_connector.getFromDB(query, val, 1)
    if id:
        return id[0][0]
    return None


def createPerson(name, gender, db_id):
    query = ("INSERT INTO person (name, gender, db_id) VALUES (%s,%s,%s)")
    val = (name, gender, db_id)
    db_connector.insertToDBWithVal(query, val)


def addPersonMovieJob(person_id, movie_id, job_id):
    query = ("INSERT INTO person_movie_job (person_id, movie_id, job_id) VALUES (%s,%s,%s)")
    val = (person_id, movie_id, job_id)
    db_connector.insertToDBWithVal(query, val)


def load_cast_and_crew(movie_id, cast, crew):
    i = 0
    for cast_member in cast:
        if (i < 10):
            name = cast_member["name"].strip()
            name = unidecode(name)
            original_name = cast_member["original_name"].strip()
            original_name = unidecode(original_name)
            person_id = checkPersonByDBID(cast_member["id"], name, original_name)
            if not person_id:
                createPerson(name, cast_member["gender"], cast_member["id"])
                person_id = db_connector.getLastInsertedId()
            addPersonMovieJob(person_id, movie_id, 1)
            i += 1

    for crew_member in crew:
        name = crew_member["name"].strip()
        name = unidecode(name)
        original_name = crew_member["original_name"].strip()
        original_name = unidecode(original_name)
        if crew_member["department"] == "Directing":
            person_id = checkPersonByDBID(crew_member["id"], name, original_name)
            if not person_id:
                createPerson(name, crew_member["gender"], crew_member["id"])
                person_id = db_connector.getLastInsertedId()
            addPersonMovieJob(person_id, movie_id, 2)


def updatePerson(id, person_gender, person_db_id):
    sql = "UPDATE person SET gender = %s,db_id = %s WHERE id = %s"
    val = (person_gender, person_db_id, id)
    db_connector.insertToDBWithVal(sql, val)


class Person:
    def __init__(self, person_id, name, gender=None, db_id=None):
        self.db_id = db_id
        self.person_id = person_id
        self.name = name
        self.gender = gender
