import os
from dotenv import load_dotenv

from requests import get
from bs4 import BeautifulSoup

load_dotenv()

GOOGLE_FORM_LINK = os.environ.get("GOOGLE_FORM_LINK")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = get(ZILLOW_URL)
response.raise_for_status()

content = response.content


def parse_price(price):
    price = (
        price.replace("+", "").replace("/mo", "").replace("1bd", "").replace("1 bd", "")
    ).strip()
    return price


soup = BeautifulSoup(content, "html.parser")

raw_listings_data = soup.find_all("div", class_="StyledPropertyCardDataWrapper")

for listing in raw_listings_data:
    price = parse_price(
        listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText()
    )
    print(price)
