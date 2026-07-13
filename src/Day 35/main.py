import os
from requests import get
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHERMAP_API_KEY = os.environ.get("OPEN_WEATHERMAP_API_KEY")


URL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "appid": OPEN_WEATHERMAP_API_KEY,
    "q": "New Delhi",
}

response = get(URL, params=parameters)
response.raise_for_status()

print(response.json())
