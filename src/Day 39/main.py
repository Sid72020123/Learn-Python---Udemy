import os
from dotenv import load_dotenv
import requests
import requests_cache

from data_manager import DataManager

load_dotenv()

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEETY_API_URL = os.environ.get("SHEETY_API_URL")
SHEETY_API_TOKEN = os.environ.get("SHEETY_API_TOKEN")


BASE_URL = "https://app.100daysofpython.dev"

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dm = DataManager(SHEETY_API_URL, SHEETY_API_TOKEN)
