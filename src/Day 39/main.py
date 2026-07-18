import os
from dotenv import load_dotenv

from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_API_URL = os.environ.get("SHEETY_API_URL")
SHEETY_API_TOKEN = os.environ.get("SHEETY_API_TOKEN")
DEPARTURE_CITY_ID = os.environ.get("DEPARTURE_CITY_ID")


dm = DataManager(SHEETY_API_URL, SHEETY_API_TOKEN)
fs = FlightSearch(APP_ID, APP_KEY, DEPARTURE_CITY_ID)

CITIES = dm.get_rows_from_sheet()

for city in CITIES:
    print(fs.get_cheapest_flight(city))
