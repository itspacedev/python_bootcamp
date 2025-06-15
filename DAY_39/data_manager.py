import requests
import os


class DataManager:

    def __init__(self):
        self.api_url = os.environ.get('SHEETY_API_URL')
        self.api_token = os.environ.get('SHEETY_TOKEN')
        self.api_sheet_path = os.environ.get('SHEETY_SHEET_PATH')

    def get_auth_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_token}"
        }

    def get_prices_data(self) -> list:
        response = requests.get(
            url=f"{self.api_url}{self.api_sheet_path}",
            headers=self.get_auth_headers()
        )
        return response.json()["prices"]

    def update_record(self, record):
        requests.put(
            url=f"{self.api_url}{self.api_sheet_path}/{record['id']}",
            json={"price": record},
            headers=self.get_auth_headers()
        )
