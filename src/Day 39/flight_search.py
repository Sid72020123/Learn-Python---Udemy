import requests
import requests_cache

from datetime import datetime, timedelta

requests_cache.install_cache("flights_api_cache")

tomorrow = datetime.now() + timedelta(days=1)
six_month_later = datetime.now() + timedelta(days=6 * 30)
print(tomorrow, six_month_later)

BASE_URL = "https://app.100daysofpython.dev"


class FlightSearch:
    def __init__(self, APP_ID, APP_KEY, DEPARTURE_CITY_ID):
        self.app_id = APP_ID
        self.api_key = APP_KEY
        self.departure_id = DEPARTURE_CITY_ID

    def search_filght(self, city_info):
        params = {
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": city_info["iataCode"],
            "outbound_date": tomorrow.strftime("%Y-%m-%d"),
            "return_date": six_month_later.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "stops": "1",
            "api_key": self.api_key,
        }

        response = requests.get(f"{BASE_URL}/v1/flights/search", params=params)
        return response.json()

    def get_cheapest_flight(self, city_info):
        flight_data = self.search_filght(city_info)
        flights = flight_data.get("best_flights", []) + flight_data.get(
            "other_flights", []
        )

        cheapest_flight = min(flights, key=lambda x: x["price"])

        return cheapest_flight
