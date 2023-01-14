import unittest
import os
from services.conversion_service import ConversionService
from services.currency_service import CurrencyService
from models.salary import Salary


class TestCurrencyService(unittest.TestCase):
    def setUp(self):
        self.currency_service = CurrencyService(
            'https://api.apilayer.com/exchangerates_data/latest', 'A3kgjT6bEobRbjQuAfdx7GcTcdD3dKqz')

    def test_get_exchange_rate(self):
        self.assertIsNotNone(
            self.currency_service.get_exchange_rate('IDR', 'USD'))


class TestConversionService(unittest.TestCase):
    def setUp(self):
        self.coversion_service = ConversionService(CurrencyService(
            'https://api.apilayer.com/exchangerates_data/latest', 'A3kgjT6bEobRbjQuAfdx7GcTcdD3dKqz'))

    def test_update_exchange_rate(self):
        self.coversion_service.update_exchange_rate('IDR', 'USD')
        # print(self.coversion_service.exchange_rate)
        self.assertNotEqual(self.coversion_service.exchange_rate, 0)

    def test_convert_salary(self):
        # test_update_exchange_rate
        self.coversion_service.update_exchange_rate('IDR', 'USD')

        # convert the salary
        file_path = (os.path.dirname(os.path.dirname(__file__))) + \
            '/data/salary_data.json'
        salary = Salary.salary_by_user_id(1, file_path)
        self.coversion_service.convert_salary(salary)
        # print(salary.converted_user_salary)
        self.assertNotEqual(salary.converted_user_salary,
                            salary.user_salary_in_IDR)
        self.assertEqual(salary.converted_currency, "USD")
