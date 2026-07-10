### --- API Basics --- ###

# from requests import get

# URL = "http://api.open-notify.org/iss-now.json"

# response = get(URL)
# response.raise_for_status()

# print(response.json())

### --- Sunrise & Sunset API --- ###

from requests import get
import datetime

URL = "https://api.sunrise-sunset.org/v2"

response = get(URL, params={"lat": 28.613939, "lng": 77.209023})
response.raise_for_status()

data = response.json()

sunrise = data["sunrise"]
sunset = data["sunset"]

print(sunrise, sunset)
