import unittest
from app.models import Person
from app.services import person as person_service


class PersonTestCase(unittest.TestCase):
    def test_filter_person_empty_input(self):
        empty_input = []
        expected = []
        self.assertEqual(person_service.filter_person(empty_input), expected)

    def test_filter_person_empty_result(self):
        people_input = [
            Person(index=0, has_died=True),
        ]
        expected = []
        self.assertEqual(person_service.filter_person(people_input), expected)

    def test_filter_person_non_empty_result(self):
        person = Person(index=0, has_died=False, eye_color='brown')
        people_input = [
            person,
        ]
        expected = [
            person,
        ]
        self.assertEqual(person_service.filter_person(people_input), expected)

    def test_get_common_friends(self):
        person1 = Person(index=0, has_died=False, eye_color='black')
        person2 = Person(index=1, has_died=True, eye_color='black')
        friend1 = Person(index=2, has_died=False, eye_color='blue')
        friend2 = Person(index=3, has_died=False, eye_color='brown')
        person1.befriend(friend1)
        person1.befriend(friend2)
        person2.befriend(friend1)

        common_friends = person_service.get_common_friends(person1, person2)
        self.assertEqual(len(common_friends), 1)
        self.assertIn(friend1, common_friends)
        self.assertNotIn(friend2, common_friends)


if __name__ == '__main__':
    unittest.main()
