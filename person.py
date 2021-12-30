import db_connector
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


class Person:
    def __init__(self, person_id, name, gender=None, original_name=None):
        self.person_id = person_id
        self.name = name
        self.gender = gender
        self.original_name = original_name
