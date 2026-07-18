import requests
import requests_cache

from flight_data import FlightData

requests_cache.install_cache("flights_api_cache")

BASE_URL = "https://app.100daysofpython.dev"


class FlightSearch:
    def __init__(self, APP_ID, APP_KEY, DEPARTURE_CITY_ID):
        self.app_id = APP_ID
        self.api_key = APP_KEY
        self.departure_id = DEPARTURE_CITY_ID

    def search_filght(self, city_info, outbound_date, return_date):
        params = {
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": city_info["iataCode"],
            "outbound_date": outbound_date,
            "return_date": return_date,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "stops": "1",
            "api_key": self.api_key,
        }

        response = requests.get(f"{BASE_URL}/v1/flights/search", params=params)
        return response.json()

    def get_cheapest_flight(self, city_info, outbound_date, return_date):
        flight_data = self.search_filght(city_info, outbound_date, return_date)
        flights = flight_data.get("best_flights", []) + flight_data.get(
            "other_flights", []
        )

        cheapest_flight = min(flights, key=lambda x: x["price"])

        return FlightData(cheapest_flight)
