from models.salary import Salary

class ConversionService:
    def __init__(self, currency_service):
        self.currency_service = currency_service
        # init value
        self.exchange_rate=1
        self.to_currency="IDR"

    def update_exchange_rate(self,  from_currency: str,to_currency: str):
        self.exchange_rate = self.currency_service.get_exchange_rate(
            from_currency, to_currency)
        self.to_currency=to_currency

    def convert_salary(self, salary: Salary):
        salary.converted_user_salary = salary.user_salary_in_IDR * self.exchange_rate
        salary.converted_currency = self.to_currency
