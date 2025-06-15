import datetime as dt


class FlightData:

    def __init__(self, flight: dict):
        self.price = 0.0
        self.departure_airport = "N/A"
        self.departure_date = "N/A"
        self.arrival_airport = "N/A"
        self.arrival_date = "N/A"
        self.parse_flight_offer(flight)

    def parse_flight_offer(self, offer):
        self.price = float(offer["price"]["total"])

        segments = offer["itineraries"][0]["segments"][0]
        self.departure_airport = segments["departure"]["iataCode"]
        self.departure_date = self.parse_date(segments["departure"]["at"])

        self.arrival_airport = segments["arrival"]["iataCode"]
        self.arrival_date = self.parse_date(segments["arrival"]["at"])

    def parse_date(self, date_str: str):
        return dt.datetime.fromisoformat(date_str)

    def print_info(self):
        print(f"Departure from {self.departure_airport} at {self.departure_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Arrival to {self.arrival_airport} at {self.arrival_date.strftime('%Y-%m-%d %H:%M')}")
        print(f"Price: GBP {self.price}")
