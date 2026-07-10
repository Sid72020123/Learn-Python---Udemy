import requests
from datetime import datetime

MY_LAT = 28.613939
MY_LONG = 77.209023

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

in_location_range = False
if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (
    iss_longitude - 5 <= MY_LONG <= iss_longitude + 5
):
    in_location_range = True


response = requests.get(
    "https://api.sunrise-sunset.org/v2", params={"lat": MY_LAT, "lng": MY_LONG}
)
response.raise_for_status()

data = response.json()
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
