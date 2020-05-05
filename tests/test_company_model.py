import unittest
from app.models import Company


class CompanyModelTestCase(unittest.TestCase):
    def test_to_dict(self):
        company = Company(index=0, name='Test')
        company_dict = company.to_dict()
        expected = {'index': 0, 'name': 'Test'}
        self.assertEqual(expected, company_dict)


if __name__ == '__main__':
    unittest.main()
