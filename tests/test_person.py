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


if __name__ == '__main__':
    unittest.main()
