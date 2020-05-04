import os
from app import create_app, db
from app.models import Person, Food, Company

import json


def run():
    """Import data from companies.json and people.json"""
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Process companies.json
        companies_to_add = []

        with open('resources/companies.json', 'r') as f:
            companies = json.load(f)
            for item in companies:
                company = Company(index=item['index'], name=item['company'])
                companies_to_add.append(company)

        db.session.add_all(companies_to_add)

        # Process people.json
        people_to_add = []
        with open('resources/people.json', 'r') as f:
            people = json.load(f)
            for item in people:
                print('Processing {}'.format(item['index']))
                # Import a person
                person = Person(index=item['index'],
                                name=item['name'],
                                has_died=item['has_died'],
                                age=item['age'],
                                eye_color=item['eyeColor'],
                                phone=item['phone'],
                                address=item['address'],
                                )

                # Assign company to person
                company = Company.query.filter_by(index=item['company_id']).first()
                if not company:
                    # If we don't have a company with this index, this person cannot be imported.
                    print('Company not found index {} for person index {} {}. Skip this item'.format(item['company_id'],
                                                                                                     item['index'],
                                                                                                     item['name']))
                    continue

                person.company = company

                # Assign food to person, also record new food item as we go
                for food_item in item['favouriteFood']:
                    food = Food.query.filter_by(name=food_item).first()
                    if not food:
                        food = Food(name=food_item, type=determine_food_type(food_item))
                    person.foods.append(food)

            # Process friendship
            for item in people:
                print('Processing {}'.format(item['index']))
                person = Person.query.filter_by(index=item['index']).first()
                if not person:
                    continue

                for friend_item in item['friends']:
                    friend = Person.query.filter_by(index=friend_item['index']).first()
                    if not friend:
                        continue
                    if person.index == friend.index:
                        continue

                    print('{} befriends {}'.format(person.index, friend.index))
                    person.befriend(friend)

                people_to_add.append(person)

        db.session.add_all(people_to_add)

        # Finalise changes to database
        db.session.commit()


def determine_food_type(food_name):
    """To determine whether a food item is a vegetable or a fruit"""
    # TODO come up with a mean to populate vegetables and fruits sets
    vegetables = {'cucumber', 'beetroot', 'carrot', 'celery', 'lettuce'}
    fruits = {'orange', 'apple', 'banana', 'strawberry'}
    if food_name in vegetables:
        return Food.VEGETABLE
    elif food_name in fruits:
        return Food.FRUIT
    else:
        return Food.UNKNOWN
