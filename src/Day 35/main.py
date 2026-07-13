import os
from pprint import pprint
from requests import get
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHERMAP_API_KEY = os.environ.get("OPEN_WEATHERMAP_API_KEY")
LOCATION = os.environ.get("LOCATION")


# URL = "https://api.openweathermap.org/data/2.5/weather"

# parameters = {
#     "appid": OPEN_WEATHERMAP_API_KEY,
#     "q": "New Delhi",
# }

# response = get(URL, params=parameters)
# response.raise_for_status()

# print(response.json())

### --- Challenge 1 --- ###

# URL = "https://api.openweathermap.org/data/2.5/forecast"

# parameters = {
#     "appid": OPEN_WEATHERMAP_API_KEY,
#     "q": LOCATION,
#     "cnt": 4,  # Only 4 timestamps (i.e., 12 hours forecast)
# }

# response = get(URL, params=parameters)
# response.raise_for_status()

# weather_data = response.json()


URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "appid": OPEN_WEATHERMAP_API_KEY,
    "q": LOCATION,
    "cnt": 4,  # Only 4 timestamps (i.e., 12 hours forecast)
}


def chances_of_rain():
    response = get(URL, params=parameters)
    response.raise_for_status()

    weather_data = response.json()
    if not weather_data["cod"] != 200:
        return

    weather_list = weather_data["list"]

    for weather_info in weather_list:
        primary_weather = weather_info["weather"][0]
        if primary_weather["id"] < 700:
            return True

    return False


print(chances_of_rain())
