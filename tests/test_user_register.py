import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain})"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playgruound.learnqa.ru/api/user", data=data)

        assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotosv@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqs',
            'lastName': 'learnqs',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)


