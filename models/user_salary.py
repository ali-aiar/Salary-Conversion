from models.salary import Salary
from models.user import User


class UserSalary:
    def __init__(self, user: User, salary: Salary):
        self.user_data = user
        self.user_salary = salary
