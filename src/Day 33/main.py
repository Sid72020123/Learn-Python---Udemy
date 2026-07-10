### --- API Basics --- ###

from requests import get

URL = "http://api.open-notify.org/iss-now.json"

response = get(URL)

response.raise_for_status()
