from app.models import Person

"""Business logic for Person endpoint"""


def get_person(person_index):
    """Get a person object given an index"""
    try:
        return Person.query.filter_by(index=person_index).first()
    except Exception as e:
        raise e


def get_common_friends(person1, person2):
    """Get common friends"""
    try:
        friends1 = set(person1.friends)
        friends2 = set(person2.friends)
        return friends1 & friends2
    except Exception as e:
        raise e


def filter_person(people, has_died=False, eye_color='brown'):
    """Filter a list of people by has_died and eye_color"""
    try:
        filtered = []
        for person in people:
            if person.has_died is has_died and person.eye_color == eye_color:
                filtered.append(person)
        return filtered
    except Exception as e:
        raise e

