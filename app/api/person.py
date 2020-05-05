from flask import jsonify
from app.api import api_blueprint
from app.services import person as person_service

"""Routes for Person"""


@api_blueprint.route('/person/common-friends/<int:person_id_1>/<int:person_id_2>')
def person_common_friends(person_id_1, person_id_2):
    """Given two people, return the list of common friends who have brown eyes and a re still alive"""
    try:
        person1 = person_service.get_person(person_id_1)
        person2 = person_service.get_person(person_id_2)
        if not person1 or not person2:
            return not_found_response()

        common_friends = person_service.get_common_friends(person1, person2)
        filtered_common_friends = person_service.filter_person(common_friends, has_died=False, eye_color='brown')

        result = {
            'person1': {
                'name': person1.name,
                'age': person1.age,
                'address': person1.address,
                'phone': person1.phone,
            },
            'person2': {
                'name': person2.name,
                'age': person2.age,
                'address': person2.address,
                'phone': person2.phone,
            },
            'common_friends': [friend.to_dict() for friend in filtered_common_friends]
        }
        return jsonify(result)
    except Exception as e:
        return exception_response()


@api_blueprint.route('/person/<int:person_id>')
def person_details(person_id):
    """Return details given a person's index"""
    try:
        person = person_service.get_person(person_id)
        if not person:
            return not_found_response()

        result = {
            'username': person.name,
            'age': person.age,
            'fruits': [food.name for food in person.foods if food.type == food.FRUIT],
            'vegetables': [food.name for food in person.foods if food.type == food.VEGETABLE],
        }

        return jsonify(result)
    except Exception as e:
        return exception_response()


def not_found_response():
    """Return not found response"""
    message = {
        'message': 'Person not found',
    }
    return jsonify(message), 404


def exception_response():
    """Return exception response"""
    message = {
        'message': 'We encountered an issue',
    }
    return jsonify(message), 500
