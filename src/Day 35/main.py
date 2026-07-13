import os
from pprint import pprint
from requests import get
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHERMAP_API_KEY = os.environ.get("OPEN_WEATHERMAP_API_KEY")


# URL = "https://api.openweathermap.org/data/2.5/weather"

# parameters = {
#     "appid": OPEN_WEATHERMAP_API_KEY,
#     "q": "New Delhi",
# }

# response = get(URL, params=parameters)
# response.raise_for_status()

# print(response.json())

### --- Challenge 1 --- ###

URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "appid": OPEN_WEATHERMAP_API_KEY,
    "q": "New Delhi",
}

response = get(URL, params=parameters)
print(response.url)
response.raise_for_status()

pprint(response.json())
