### --- API Basics --- ###

# from requests import get

# URL = "http://api.open-notify.org/iss-now.json"

# response = get(URL)
# response.raise_for_status()

# print(response.json())

### --- Sunrise & Sunset API --- ###

from requests import get

URL = "https://api.sunrise-sunset.org/v2"

response = get(URL, params={"lat": -82.862755, "lng": 135.000000})
response.raise_for_status()

print(response.json())
