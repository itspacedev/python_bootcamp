import os
import requests
import datetime as dt
from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ.get('AMADEUS_API_KEY')
        self.api_secret = os.environ.get('AMADEUS_API_SECRET')
        self.token = self.get_new_token()

    def get_new_token(self) -> str:
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            }
        )
        response_json = response.json()
        return response_json["access_token"]

    def get_iata_code(self, city_name: str) -> str:
        response = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            params={
                "keyword": city_name
            }
        )
        locations = response.json()["data"]

        # Just return the code from the first location to eliminate complex logic for now
        return locations[0]['iataCode']

    def find_cheapest_flight(self, from_code: str, to_code: str):
        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            params={
                "originLocationCode": from_code,
                "destinationLocationCode": to_code,
                "departureDate": dt.datetime.now().strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": 10
            }
        )
        response_json = response.json()
        cheapest_offer = None
        if "data" in response_json:
            flight_offers = response_json["data"]
            for flight_offer in flight_offers:
                offer = FlightData(flight_offer)
                if cheapest_offer is None or offer.price < cheapest_offer.price:
                    cheapest_offer = offer

        return cheapest_offer




