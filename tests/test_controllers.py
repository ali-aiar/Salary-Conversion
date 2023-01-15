import unittest
import os
from controllers.conversion_controller import ConversionController
from controllers.salary_controller import SalaryController
from services.conversion_service import ConversionService
from services.currency_service import CurrencyService
from models.salary import Salary
from models.user import User


class TestConversionController(unittest.TestCase):
    def setUp(self):
        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/salary_data.json'
        salary = Salary.salary_by_user_id(1, file_path)
        coversion_service = ConversionService(CurrencyService(
            'https://api.apilayer.com/exchangerates_data/latest',
            'A3kgjT6bEobRbjQuAfdx7GcTcdD3dKqz'))

        self.conversion_controller = ConversionController(
            coversion_service, salary, file_path, 'IDR', 'USD')
        self.assertNotEqual(self.conversion_controller.salary.currency,
                            self.conversion_controller.salary.converted_currency)

    def test_convert_salary(self):
        salary = self.conversion_controller.convert_salary(1)
        self.assertNotEqual(salary.converted_user_salary,
                            salary.user_salary_in_IDR)


class TestSalaryController(unittest.TestCase):
    def setUp(self):
        user = User.fetch_users(
            'http://jsonplaceholder.typicode.com/users')
        salary = Salary

        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/salary_data.json'
        salary = Salary.salary_by_user_id(1, file_path)
        conversion_service = ConversionService(CurrencyService(
            'https://api.apilayer.com/exchangerates_data/latest',
            'A3kgjT6bEobRbjQuAfdx7GcTcdD3dKqz'))

        self.salary_controller = SalaryController(
            user, salary, conversion_service, file_path, 'IDR', 'USD')

    def test_get_all(self):
        data = self.salary_controller.get_all()
        for i in range(5):
            print(
                f"id: {data[i].user_data.id}, salary: $ {data[i].user_salary.converted_user_salary}")
        self.assertEqual(data[0].user_data.id, 1)
