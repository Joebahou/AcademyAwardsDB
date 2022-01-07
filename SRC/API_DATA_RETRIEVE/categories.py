from SRC import db_connector
from SRC import utils

Animated_Feature_Film = "Animated Feature Film"
Art_Direction = "Art Direction"
Cinematography = "Cinematography"
Costume_Design = "Costume Design"
Documentary_Feature = "Documentary (Feature)"
Documentary_Short = "Documentary (Short Subject)"
Film_Editing = "Film Editing"
Foreign_Language_Film = "Foreign Language Film"
Makeup = "Makeup"
Music_Scoring = "Music (Scoring)"
Music_Song = "Music (Song)"
Best_Picture = "Best Picture"
Short_Film_Animated = "Short Film (Animated)"
Short_Film_Live = "Short Film (Live Action)"
Sound = "Sound"
Sound_Editing = "Sound Editing"
Visual_Effects = "Visual Effects"
Writing = "Writing"
Actor_Leading_Role = "Actor -- Leading Role"
Actor_Supporting_Role = "Actor -- Supporting Role"
Actress_Leading_Role = "Actress -- Leading Role"
Actress_Supporting_Role = "Actress -- Supporting Role"
Directing = "Directing"


def isInCategories(category):
    return (category in Categories.categoriesForPerson) or (category in Categories.categoriesForMovies)


def isCategoryExistsInDB(category):
    categories = getCategoriesByName(category)
    return len(categories) > 0


def getCategoriesByName(category_name):
    query = """SELECT * FROM oscarCategory WHERE category = "%s" """ % category_name
    categories_from_db = db_connector.getFromDB(query)
    categories = []
    for cat in categories_from_db:
        category = Category(cat[0], cat[1])
        categories.append(category)
    return categories


def getHighestCategoryID():
    query = """SELECT MAX(id) FROM oscarCategory"""
    highest_id = db_connector.getFromDB(query, 1)
    return utils.getNumOrZeroIfNone(highest_id)


class Category:
    def __init__(self, category_id, name):
        self.name = name
        self.category_id = category_id


class Categories:
    categoriesForMovies = {Animated_Feature_Film,
                           Art_Direction,
                           Cinematography,
                           Costume_Design,
                           Documentary_Feature,
                           Documentary_Short,
                           Film_Editing,
                           Foreign_Language_Film,
                           Makeup,
                           Music_Scoring,
                           Music_Song,
                           Best_Picture,
                           Short_Film_Animated,
                           Short_Film_Live,
                           Sound,
                           Sound_Editing,
                           Visual_Effects,
                           Writing,
                           }

    categoriesForPerson = {Actor_Leading_Role,
                           Actress_Leading_Role,
                           Actor_Supporting_Role,
                           Actress_Supporting_Role,
                           Directing
                           }
