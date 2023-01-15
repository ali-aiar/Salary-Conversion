import requests


class CurrencyService:
    def __init__(self, exchange_rate_api_url: str, exchange_rate_api_key: str):
        self.exchange_rate_api_url = exchange_rate_api_url
        self.exchange_rate_api_key = exchange_rate_api_key

    def get_exchange_rate(self, from_currency: str, to_currency: str):
        headers = {'apikey': self.exchange_rate_api_key}
        response = requests.get(
            f'{self.exchange_rate_api_url}?symbols={to_currency}&base={from_currency}', headers=headers)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['rates'][to_currency]
            return exchange_rate
        else:
            raise Exception('Failed to get exchange rate')
