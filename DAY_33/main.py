import requests
import datetime as dt
import smtplib

ISS_ENDPOINT_URL = "http://api.open-notify.org/iss-now.json"
MY_LAT = 0.0000000
MY_LNG = 0.0000000

SMTP_SERVER = "smtp.gmail.com"
SMTP_USER = "*************"
SMTP_PASSWORD = "*************"


def is_iss_overhead():
    response = requests.get(url=ISS_ENDPOINT_URL)
    response.raise_for_status()
    iss_data = response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5):
        return True
    else:
        return False


def is_night():
    parameters = {
        "lng": MY_LNG,
        "lat": MY_LAT,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()
    now_hour = time_now.hour
    if now_hour >= sunset or now_hour <= sunrise:
        return True
    else:
        return False


if is_iss_overhead() and is_night():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SMTP_USER, password=SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_USER,
            to_addrs=SMTP_USER,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky!"
        )
