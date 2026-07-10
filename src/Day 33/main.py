import os
from time import sleep
import requests
from datetime import datetime

import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

### ------ CONFIG ------ ###

load_dotenv()
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))
USERNAME = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("SMTP_KEY")
SENDER_EMAIL = os.environ.get("EMAIL_FROM")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

last_range_status = False


def send_alert_email():
    msg = EmailMessage()
    msg["Subject"] = "ISS Overhead Alert!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = (
        RECIPIENT_EMAIL  # can use the 'email' var here but keeping the default ENV value for privacy reasons...
    )
    msg.set_content(
        "ISS is above you (in the sky) in your location range!\n\nLook above!"
    )

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")


MY_LAT = 19.054999
MY_LONG = 72.869203

while True:
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        in_location_range = False
        if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        ):
            in_location_range = True

        response = requests.get(
            "https://api.sunrise-sunset.org/v2", params={"lat": MY_LAT, "lng": MY_LONG}
        )
        response.raise_for_status()

        data = response.json()
        sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        hour_now = time_now.hour

        is_dark = False
        if hour_now >= sunset or hour_now <= sunrise:
            is_dark = True

        print("In range?", in_location_range)
        print("Is dark?", is_dark)
        print(
            f"Current Position: Lat > {iss_latitude} Long > {iss_longitude} [{iss_latitude}, {iss_longitude}]"
        )

        if is_dark and in_location_range and (last_range_status is False):
            send_alert_email()

        last_range_status = in_location_range
        print("-" * 50)
    except Exception as E:
        print("Exception:", E)
    sleep(60)  # Check every 1 minute
