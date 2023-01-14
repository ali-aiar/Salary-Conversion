from models.salary import Salary
from models.user import User
from models.user_salary import UserSalary
from controllers.conversion_controller import ConversionController
from services.conversion_service import ConversionService


class SalaryController:
    def __init__(self, user: User, salary: Salary, conversion_service: ConversionService,  json_path: str, from_currency: str, to_currency: str):
        self.user_salary = UserSalary(user, salary)
        self.conversion_control = ConversionController(
            conversion_service, salary, json_path, from_currency, to_currency)

    def get_all(self):
        users_salary = []
        for user in self.user_salary.user_data:
            # print(user)
            users_salary.append(UserSalary(
                user, self.conversion_control.convert_salary(user.id)))
        return users_salary
