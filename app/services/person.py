from app.models import Person

"""Business logic for Person endpoint"""


def get_person(person_index):
    """Get a person object given an index"""
    return Person.query.filter_by(index=person_index).first()


def get_common_friends(person1, person2):
    """Get common friends"""
    friends1 = set(person1.friends)
    friends2 = set(person2.friends)
    return friends1 & friends2


def filter_person(people, has_died=False, eye_color='brown'):
    """Filter a list of people by has_died and eye_color"""
    filtered = []
    for person in people:
        if person.has_died is has_died and person.eye_color == eye_color:
            filtered.append(person)
    return filtered

