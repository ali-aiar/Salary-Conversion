import json


class Salary:
    def __init__(self, id: int, user_salary_in_IDR: float):
        self.id = id
        self.user_salary_in_IDR = user_salary_in_IDR
        self.currency = 'IDR'
        self.converted_user_salary = 0
        self.converted_currency = 'USD'

    @classmethod
    def from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(data['id'], data['salaryInIDR'])

    @classmethod
    def salary_by_user_id(cls, user_id: int, json_file: str):
        with open(json_file, 'r') as f:
            data = json.load(f)
            for salary in data['array']:
                if salary['id'] == user_id:
                    return cls.from_json(json.dumps(salary))
