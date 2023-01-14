from services.conversion_service import ConversionService
from models.salary import Salary


class ConversionController:
    def __init__(self, conversion_service: ConversionService, salary: Salary, json_path: str, from_currency: str, to_currency: str):
        self.conversion_service = conversion_service
        self.salary = salary
        self.json_file = json_path
        self.conversion_service.update_exchange_rate(
            from_currency, to_currency)

    def update_rate(self, from_currency: str, to_currency: str):
        self.conversion_service.update_exchange_rate(
            from_currency, to_currency)

    def convert_salary(self,  salary_id: int):
        salary = self.get_salary(salary_id)
        self.conversion_service.convert_salary(salary)
        return salary

    def get_salary(self, salary_id: int):
        # Retrieve the salary from the data salary_data.json
        return self.salary.salary_by_user_id(salary_id, self.json_file)
