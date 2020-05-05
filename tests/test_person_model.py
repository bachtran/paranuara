import unittest
from app.models import Person, Food


class MyTestCase(unittest.TestCase):
    def test_befriend(self):
        person = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        friend = Person(index=1, name='Friend', age=30, has_died=False, eye_color='blue', phone='000', address='test')
        person.befriend(friend)
        self.assertEqual(len(person.friends), 1)
        self.assertEqual(person.friends[0].to_dict(), friend.to_dict())

    def test_unfriend(self):
        person = Person(index=0, name='Test', age=30, has_died=False, eye_color='black', phone='000', address='test')
        friend = Person(index=1, name='Friend', age=30, has_died=False, eye_color='blue', phone='000', address='test')
        person.befriend(friend)
        person.unfriend(friend)
        self.assertEqual(len(person.friends), 0)

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
        self.assertEqual(person_dict, expected)


if __name__ == '__main__':
    unittest.main()
