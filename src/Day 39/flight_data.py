class FlightData:
    def __init__(self, flight_info):
        self.flight = flight_info["flights"][0]

        self.arrival_airport_id = self.flight["arrival_airport"]["id"]
        self.arrival_time = self.flight["arrival_airport"]["time"]

        self.departure_airport_id = self.flight["departure_airport"]["id"]
        self.departure_time = self.flight["departure_airport"]["time"]

        self.price = flight_info["price"]
