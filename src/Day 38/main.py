import os
from dotenv import load_dotenv
from requests import post

load_dotenv()

### --- CONFIG --- ###

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

BASE_URL = "https://app.100daysofpython.dev"

### --- DATA --- ###

data = {"query": "ran for 30 minutes"}

response = post(f"{BASE_URL}/v1/nutrition/natural/exercise", headers=headers, json=data)
response.raise_for_status()

print(response.json())
