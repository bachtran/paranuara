import unittest
from app import create_app, db
from app.models import Person, Company, Food


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.set_up_test_db()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @staticmethod
    def set_up_test_db():
        person1 = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        person2 = Person(index=1, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        friend = Person(index=2, name='Friend', age=30, has_died=False, eye_color='brown', phone='000', address='test')
        company = Company(index=0, name='Test')
        no_employees_company = Company(index=1, name='No Employees')
        vegetable = Food(index=0, name='Lettuce', type=Food.VEGETABLE)
        fruit = Food(index=1, name='Banana', type=Food.FRUIT)

        person1.company = company
        person1.foods.append(vegetable)
        person1.foods.append(fruit)
        person2.company = company
        person1.befriend(friend)
        person2.befriend(friend)

        db.session.add(person1)
        db.session.add(no_employees_company)

    def test_get_company_invalid_index(self):
        response = self.client.get('/api/v1/company/100')
        self.assertEqual(404, response.status_code)

    def test_get_company_valid_index(self):
        response = self.client.get('/api/v1/company/0')
        self.assertEqual(200, response.status_code)
        expected = {'index': 0, 'name': 'Test'}
        self.assertEqual(expected, response.get_json())

    def test_get_company_employees_invalid_index(self):
        response = self.client.get('/api/v1/company/100')
        self.assertEqual(404, response.status_code)

    def test_get_company_employees_valid_index(self):
        response = self.client.get('/api/v1/company/0/employees')
        self.assertEqual(200, response.status_code)
        expected = [{'address': 'test', 'age': 30, 'eye_color': 'black', 'has_died': False,
                     'index': 0, 'name': 'Test', 'phone': '000'},
                    {'address': 'test', 'age': 30, 'eye_color': 'black', 'has_died': False,
                     'index': 1, 'name': 'Test', 'phone': '000'}]
        self.assertEqual(expected, response.get_json())

    def test_get_company_employees_no_employees(self):
        response = self.client.get('/api/v1/company/1/employees')
        self.assertEqual(200, response.status_code)
        expected = {'message': 'This company does not have any employees'}
        self.assertEqual(expected, response.get_json())

    def test_get_person_invalid_index(self):
        response = self.client.get('/api/v1/person/100')
        self.assertEqual(404, response.status_code)

    def test_get_person_valid_index(self):
        response = self.client.get('/api/v1/person/0')
        self.assertEqual(200, response.status_code)
        expected = {'age': 30, 'fruits': ['Banana'], 'username': 'Test', 'vegetables': ['Lettuce']}
        self.assertEqual(expected, response.get_json())

    def test_get_common_friends_invalid_index(self):
        response = self.client.get('/api/v1/person/common-friends/0/100')
        self.assertEqual(404, response.status_code)

    def test_get_common_friends_valid_index(self):
        response = self.client.get('/api/v1/person/common-friends/0/1')
        self.assertEqual(200, response.status_code)
        expected = {'common_friends': [{'address': 'test', 'age': 30, 'eye_color': 'brown', 'has_died': False,
                                        'index': 2, 'name': 'Friend', 'phone': '000'}],
                    'person1': {'address': 'test', 'age': 30, 'name': 'Test', 'phone': '000'},
                    'person2': {'address': 'test', 'age': 30, 'name': 'Test', 'phone': '000'}}
        self.assertEqual(expected, response.get_json())


if __name__ == '__main__':
    unittest.main()
