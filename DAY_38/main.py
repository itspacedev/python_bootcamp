import requests
import datetime as dt
from prettytable import PrettyTable

MY_WEIGHT = 75
MY_HEIGHT = 180
MY_AGE = 24

# Nutritionix.com settings
NUTRITION_URL = "https://trackapi.nutritionix.com"
NUTRITION_APP = "**********"
NUTRITION_APIKEY = "**********"

# An authentication token to perform GET/POST requests to Sheety APIs
SHEETY_TOKEN = "**********"
# A path for an Excel sheet document on Sheety Platform
SHEETY_SHEET_PATH = "**********"


def get_workouts_data():
    """
    Uses Nutrition API to get detailed information on the workouts that user inputs
    """
    e_text = input("Tell me what exercises you did: ")

    request_headers = {
        "Content-Type": "application/json",
        "x-app-id": NUTRITION_APP,
        "x-app-key": NUTRITION_APIKEY
    }
    request_json = {
        "query": e_text,
        "weight_kg": MY_WEIGHT,
        "height_cm": MY_HEIGHT,
        "age": MY_AGE,
    }

    response = requests.post(
        url=f"{NUTRITION_URL}/v2/natural/exercise",
        json=request_json,
        headers=request_headers
    )
    exercises = response.json()["exercises"]
    exercises_formatted = []
    for e in exercises:
        exercises_formatted.append({
            "exercise": e["name"],
            "duration": e["duration_min"],
            "calories": e["nf_calories"],
        })
    return exercises_formatted


def add_workouts_to_excel_sheet(workouts_list):
    """
    Adds the workouts' information to a Google Sheet file
    """
    date = dt.datetime.now().strftime("%d/%m/%Y")
    request_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    for workout in workouts_list:
        request_json = {
            "workout": {
                "date": date,
                "time": "19:00:00",
                "exercise": workout["exercise"],
                "duration": workout["duration"],
                "calories": workout["calories"],
            }
        }
        response = requests.post(
            url=f"https://api.sheety.co/{SHEETY_SHEET_PATH}",
            json=request_json,
            headers=request_headers
        )
        # print(response.text)


def print_workouts_from_excel():
    """
    Gets workouts' data from a Google Sheet and prints it in a pretty table form
    """
    request_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    response = requests.get(
        url=f"https://api.sheety.co/{SHEETY_SHEET_PATH}",
        headers=request_headers
    )
    workouts = response.json()["workouts"]
    # print(workouts)

    table = PrettyTable()
    table.field_names = ["Date", "Time", "Exercise", "Duration", "Calories"]
    for workout in workouts:
        table.add_row([workout["date"], workout["time"], workout["exercise"], workout["duration"], workout["calories"]])

    print(table)


# workouts = get_workouts_data()
# add_workouts_to_excel_sheet(workouts)
print_workouts_from_excel()

