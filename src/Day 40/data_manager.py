import requests
import requests_cache

requests_cache.install_cache("sheety_api_cache")


class DataManager:
    def __init__(self, SHEETY_API_URL, SHEETY_API_TOKEN):
        self.SHEETY_API_URL = SHEETY_API_URL
        self.headers = {"Authorization": f"Bearer {SHEETY_API_TOKEN}"}

    def get_rows_from_sheet(self):
        response = requests.get(self.SHEETY_API_URL, headers=self.headers)
        return response.json()["prices"]

    def update_price(self, row_id, new_price):
        data = {"price": {"lowestPrice": new_price}}
        response = requests.put(
            f"{self.SHEETY_API_URL}/{row_id}", headers=self.headers, json=data
        )
        return response
