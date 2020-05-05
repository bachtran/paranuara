import unittest
from app.models import Person, Food


class MyTestCase(unittest.TestCase):
    def test_befriend(self):
        person = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        friend = Person(index=1, name='Friend', age=30, has_died=False, eye_color='blue', phone='000', address='test')
        person.befriend(friend)
        self.assertEqual(1, len(person.friends))
        self.assertEqual(person.friends[0].to_dict(), friend.to_dict())

    def test_unfriend(self):
        person = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        friend = Person(index=1, name='Friend', age=30, has_died=False, eye_color='blue', phone='000', address='test')
        person.befriend(friend)
        person.unfriend(friend)
        self.assertEqual(0, len(person.friends))

    def test_to_dict(self):
        person = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        person_dict = person.to_dict()
        expected = {'index': 0,
                    'name': 'Test',
                    'age': 30,
                    'has_died': False,
                    'eye_color': 'black',
                    'phone': '000',
                    'address': 'test',
                    }
        self.assertEqual(expected, person_dict)


if __name__ == '__main__':
    unittest.main()
