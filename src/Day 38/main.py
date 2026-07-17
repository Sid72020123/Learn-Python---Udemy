import os
from dotenv import load_dotenv
from requests import post
import datetime

load_dotenv()

### --- CONFIG --- ###

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETS_API_URL = os.environ.get("SHEETS_API_URL")
SHEETS_API_TOKEN = os.environ.get("SHEETS_API_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

BASE_URL = "https://app.100daysofpython.dev"

### --- DATA from NLP --- ###

data = {"query": input("What exercises did you do today? ")}

response = post(f"{BASE_URL}/v1/nutrition/natural/exercise", headers=headers, json=data)
response.raise_for_status()

result = response.json()

### --- Save DATA to Google Sheets --- ###

date_today = datetime.datetime.now().strftime("%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%X")

headers = {"Authorization": f"Bearer {SHEETS_API_TOKEN}"}

for exercise in result["exercises"]:
    data = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = post(SHEETS_API_URL, json=data)

    print(response.text)
