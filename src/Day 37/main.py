import os
from requests import get, post
from dotenv import load_dotenv
from time import strftime

load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sid72020123"
GRAPH_ID = "test-graph"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a user
# pixela_endpoint = "https://pixe.la/v1/users"
# response = post(pixela_endpoint, json=user_params)

# print(response.text)

### --- Creating a graph ---
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": "test-graph",
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai",
# }

# headers = {"X-USER-TOKEN": PIXELA_TOKEN}

# response = post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

## --- Updating / Adding elements to a graph ---

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixela_data = {
    "date": strftime("%Y%m%d"),
    "quantity": "5",
}

headers = {"X-USER-TOKEN": PIXELA_TOKEN}

response = post(graph_endpoint, json=pixela_data, headers=headers)
print(response.text)
