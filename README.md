# Paranuara Challenge
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and
reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

The government from Paranuara will provide you two json files (located at resource folder) which will provide information about all the citizens in Paranuara (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

## Delivery
To deliver your system, you need to send the link on GitHub. Your solution must provide tasks to install dependencies, build the system and run. Solutions that does not fit this criteria **will not be accepted** as a solution. Assume that we have already installed in our environment Java, Ruby, Node.js, Python, MySQL, MongoDB and Redis; any other technologies required must be installed in the install dependencies task. Moreover well tested and designed systems are one of the main criteria of this assessement 

## Evaluation criteria
- Solutions written in Python would be preferred.
- Installation instructions that work.
- During installation, we may use different companies.json or people.json files.
- The API must work.
- Tests

Feel free to reach to your point of contact for clarification if you have any questions.

# Implementation
This is the implementation for the Paranuara Challenge. The implementation makes use of python3, flask and SQLAlchemy.

## Design assumption
### Data model design
- Relational model
- ERD here
### Data processing and import
- Skip invalid user records (such as those with invalid company index).
- Also skip invalid friendship to oneself.
- Preload the food types to split food item into vegetables and fruits.

### Endpoints
#### Company
- Company's details `/api/v1/company/<company_id>`
- Company's employees `/api/v1/company/<company_id>/employees`
#### Person
- Person's details `/api/v1/person/<person_id>`
- Common friends of two people `/api/v1/person/common-friends/<person_id_1>/<person_id_2>`

## Installation
Using virtualenv or docker
### Virtualenv
- `git clone https://github.com/bachtran/paranuara.git`
- `cd paranuara`
- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install -r requirements.txt`
- `export FLASK_APP=paranuara.py`
- To test `flask test`
- To import data (companies.json and people.json in resources directory) `flask import-data`
- To run the app `flask run`
### Docker
- `git clone https://github.com/bachtran/paranuara.git`
- `cd paranuara`
- `docker-compose up`

