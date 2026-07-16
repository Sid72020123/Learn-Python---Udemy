import os
from requests import get, post
from dotenv import load_dotenv

load_dotenv()

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")

user_params = {
    "token": PIXELA_TOKEN,
    "username": "Sid72020123",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a user
pixela_endpoint = "https://pixe.la/v1/users"
response = post(pixela_endpoint, json=user_params)
response.raise_for_status()

print(response.json())
