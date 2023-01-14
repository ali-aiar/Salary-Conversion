import requests


class User:
    def __init__(self, id: int, name: str, username: str, email: str, address: str, phone: str):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone

    def fetch_users(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            users_data = response.json()
            users = []
            for data in users_data:
                # address=
                users.append(
                    User(data['id'], data['name'], data['username'], data['email'], data['address'], data['phone']))
            return users
        else:
            raise Exception('Failed to retreive users')
