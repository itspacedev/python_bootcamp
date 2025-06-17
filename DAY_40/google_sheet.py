import os
import requests
from user_data import UserData


class GoogleSheet:

    def __init__(self):
        self._api_url = os.environ.get('SHEETY_API_URL')
        self._api_token = os.environ.get('SHEETY_API_TOKEN')
        self._document_path = os.environ.get('SHEETY_DOCUMENT_PATH')

    def authorization_headers(self):
        return {
            "Authorization": f"Bearer {self._api_token}"
        }

    def get_users(self):
        response = requests.get(
            url=f"{self._api_url}/{self._document_path}/users",
            headers=self.authorization_headers()
        )
        return response.json()["users"]

    def find_user_by_email(self, email):
        existing_users = self.get_users()
        for user in existing_users:
            if user['email'].lower() == email.lower():
                return UserData(user['firstName'], user['lastName'], user['email'], user['city'])
        return None

    def create_new_user(self, user: UserData):
        response = requests.post(
            url=f"{self._api_url}/{self._document_path}/users",
            json={
                "user": {
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "email": user.email,
                    "city": user.city
                }
            },
            headers=self.authorization_headers()
        )
        user = response.json()["user"]
        return UserData(user['firstName'], user['lastName'], user['email'], user['city'])

    def get_cities(self):
        response = requests.get(
            url=f"{self._api_url}/{self._document_path}/prices",
            headers=self.authorization_headers()
        )
        return response.json()["prices"]

    def get_city_iata_code(self, city_name):
        existing_cities = self.get_cities()
        for city in existing_cities:
            if city['city'].lower() == city_name.lower() and len(city['iataCode']) > 0:
                return city['iataCode']
        return None

    def create_new_city(self, city, iata_code):
        response = requests.post(
            url=f"{self._api_url}/{self._document_path}/prices",
            json={
                "price": {
                    "city": city,
                    "iataCode": iata_code,
                    "lowestPrice": "0.0"
                }
            },
            headers=self.authorization_headers()
        )
        # print(response.text)
