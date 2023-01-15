import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.USER_DATA_API = os.getenv('USER_DATA_API')
        self.EXCHANGE_RATE_API_URL = os.getenv('EXCHANGE_RATE_API_URL')
        self.EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')


config = {
    'default': Config()
}
