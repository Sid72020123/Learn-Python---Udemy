import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

headers = {"x-api-key": API_KEY, "x-app-id": APP_ID}
