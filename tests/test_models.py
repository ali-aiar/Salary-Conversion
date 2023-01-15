import unittest
import os
from models.salary import Salary
from models.user import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User.fetch_users(
            'http://jsonplaceholder.typicode.com/users')

    def test_user_id(self):
        self.assertEqual(self.user[0].id, 1)

    def test_user_addres(self):
        self.assertEqual(self.user[0].address['city'], 'Gwenborough')


class TestSalaryModel(unittest.TestCase):
    def test_get_salary_by_id(self):
        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/salary_data.json'
        data = Salary.salary_by_user_id(1, file_path)
        self.assertEqual(data.user_salary_in_IDR, 4.001111510555328e6)
        self.assertEqual(data.currency, 'IDR')
