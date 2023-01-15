import os
from PyQt6.QtWidgets import QApplication

from config import config

from controllers.conversion_controller import ConversionController
from controllers.salary_controller import SalaryController

from services.conversion_service import ConversionService
from services.currency_service import CurrencyService

from models.salary import Salary
from models.user import User

from views.salary_view import SalaryView


config = config['default']
file_path = (os.path.dirname(__file__)) + '/data/salary_data.json'

user = User.fetch_users(config.USER_DATA_API)
salary = Salary

conversion_service = ConversionService(CurrencyService(config.EXCHANGE_RATE_API_URL,
                                                       config.EXCHANGE_RATE_API_KEY))

salary_controller = SalaryController(
    user, salary, conversion_service, file_path, 'IDR', 'USD')

if __name__ == '__main__':
    app = QApplication([])
    salary_data = salary_controller.get_all()

    salary_view = SalaryView(salary_data)
    salary_view.show()
    app.exec()
