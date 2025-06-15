import os
import datetime as dt
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

# Load environment variables from .env file
load_dotenv()

# Create an instance of the DataManager class
data_manager = DataManager()

# Create an instance of the FlightSearch class
flight_search = FlightSearch()

# Use AMADEUS APIs to fetch IATA codes for cities
cities = data_manager.get_prices_data()
for city in cities:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_iata_code(city["city"])
        data_manager.update_record(city)

# Search for cheap flights for the cities in our Google Sheet
for city in cities:
    print(f"Looking for cheap flights from London to {city['city']}\n")
    cheapest_flight = flight_search.find_cheapest_flight("LON", city["iataCode"])
    if cheapest_flight is not None:
        cheapest_flight.print_info()
    else:
        print(f"There are no flights between London and {city['city']} on that date")

    print("")
