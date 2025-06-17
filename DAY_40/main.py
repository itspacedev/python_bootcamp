import os
from dotenv import load_dotenv
from user_data import UserData
from google_sheet import GoogleSheet
from flight_api import FlightApi

# Load Environment variables
load_dotenv()

print("Welcome to the Flight Club APP :)")

google_sheet = GoogleSheet()
flight_api = FlightApi()

# Ask user to input the email address
user_email = ""
while len(user_email) == 0:
    user_email = input("What is your email address?: ").strip().lower()

# Check if the user exists with this email
user = google_sheet.find_user_by_email(user_email)
if user is not None:
    print(f"Welcome back, {user.full_name()}")
# Create a new user otherwise
else:
    user_first_name = ""
    user_last_name = ""
    user_city = ""
    user_city_iata_code = None

    while len(user_first_name) == 0:
        user_first_name = input("What is your First name?: ").strip().title()

    while len(user_last_name) == 0:
        user_last_name = input("What is your Last name?: ").strip().title()

    while len(user_city) == 0:
        user_city = input("What is the name of the city you are currently in?: ").strip().title()

    user = google_sheet.create_new_user(UserData(user_first_name, user_last_name, user_email, user_city))

    print(f"You are very welcome to our Flight Club, {user.full_name()}")

# Check if the IATA code is available for the user's city
departure_iata_code = google_sheet.get_city_iata_code(user.city)
if departure_iata_code is None:
    print(f"Searching for IATA code for {user.city}")
    departure_iata_code = flight_api.get_city_iata_code(user.city)
    print(f"Found IATA code for {user.city}, which is {departure_iata_code}")
    google_sheet.create_new_city(user.city, departure_iata_code)
else:
    print(f"IATA code for {user.city} exists, and it is {departure_iata_code}")

# Ask user what city he wants to go and check IATA code for that city
destination_location = ""
while len(destination_location) == 0:
    destination_location = input("Where you would like to go? Enter the name of the city: ").strip().title()

destination_iata_code = google_sheet.get_city_iata_code(destination_location)
if destination_iata_code is None:
    print(f"Searching for IATA code for {destination_location}")
    destination_iata_code = flight_api.get_city_iata_code(destination_location)
    print(f"Found IATA code for {destination_location}, which is {destination_iata_code}")
    google_sheet.create_new_city(destination_location, destination_iata_code)
else:
    print(f"IATA code for {destination_location} exists, and it is {destination_iata_code}")


print("")
print(f"Searching flights from {departure_iata_code} ({user.city}) to {destination_iata_code} ({destination_location}) ...")
flights = flight_api.get_flights_offers(departure_iata_code, destination_iata_code)
if len(flights) > 0:
    print(f"We have found {len(flights)} offers for you: ")
    for flight in flights:
        print("")
        flight.print_info()
else:
    print(f"Sorry, we could not find any flights from {departure_iata_code} ({user.city}) to {destination_iata_code} ({destination_location})")
