import os
import datetime as dt
import requests
from flight_data import FlightData


class FlightApi:

    def __init__(self):
        self._api_url = os.environ.get('AMADEUS_API_URL')
        self._api_key = os.environ.get('AMADEUS_API_KEY')
        self._api_secret = os.environ.get('AMADEUS_API_SECRET')
        self._api_token = self.get_new_token()

    def get_new_token(self) -> str:
        response = requests.post(
            url=f"{self._api_url}/v1/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "client_credentials",
                "client_id": self._api_key,
                "client_secret": self._api_secret
            }
        )
        response_json = response.json()
        return response_json["access_token"]

    def get_city_iata_code(self, city):
        response = requests.get(
            url=f"{self._api_url}/v1/reference-data/locations/cities",
            headers={
                "Authorization": f"Bearer {self._api_token}"
            },
            params={
                "keyword": city
            }
        )
        locations = response.json()["data"]
        if len(locations) > 0:
            # Just return the code from the first location to eliminate complex logic for now
            return locations[0]['iataCode']
        else:
            return None

    def get_cheapest_flight(self, from_iata_code: str, to_iata_code: str, direct: bool):
        in_one_week = dt.datetime.now() + dt.timedelta(days=7)
        search_params = {
            "originLocationCode": from_iata_code,
            "destinationLocationCode": to_iata_code,
            "departureDate": in_one_week.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if direct else "false",
            "currencyCode": "GBP",
            "max": 10
        }

        response = requests.get(
            url=f"{self._api_url}/v2/shopping/flight-offers",
            headers={
                "Authorization": f"Bearer {self._api_token}"
            },
            params=search_params
        )
        cheapest_flight = None
        response_json = response.json()
        if "data" in response_json:
            flight_offers = response_json["data"]
            for flight_offer in flight_offers:
                offer = FlightData(flight_offer)
                if cheapest_flight is None or offer.price < cheapest_flight.price:
                    cheapest_flight = offer

        return cheapest_flight

    def get_flights_offers(self, from_iata_code: str, to_iata_code: str):
        available_flights = []

        # Search for the cheapest direct flight
        cheapest_direct_flight = self.get_cheapest_flight(from_iata_code, to_iata_code, direct=True)
        if cheapest_direct_flight is not None:
            available_flights.append(cheapest_direct_flight)

        # Search for the cheapest flight with stops
        cheapest_flight_with_stops = self.get_cheapest_flight(from_iata_code, to_iata_code, direct=False)
        if cheapest_flight_with_stops is not None:
            available_flights.append(cheapest_flight_with_stops)

        return available_flights
