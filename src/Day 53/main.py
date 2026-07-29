import os
from time import sleep
from dotenv import load_dotenv

from requests import get
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()

GOOGLE_FORM_LINK = os.environ.get("GOOGLE_FORM_LINK", "")
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keep the browser open

driver = webdriver.Chrome(options=chrome_options)

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

LISTINGS_DATA = []

for listing in raw_listings_data:
    address_info = listing.find("a", class_="StyledPropertyCardDataArea-anchor")
    address = address_info.getText().replace("|", "").replace("\n", "").strip()
    link = address_info["href"]
    price = parse_price(
        listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText()
    )
    print(link, address, price)
    LISTINGS_DATA.append({"address": address, "link": link, "price": price})

print(LISTINGS_DATA)

for data in LISTINGS_DATA:
    driver.get(GOOGLE_FORM_LINK)
    sleep(2)

    address_input = driver.find_element(
        By.CSS_SELECTOR,
        "div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)",
    )
    price_input = driver.find_element(
        By.CSS_SELECTOR,
        "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)",
    )
    link_input = driver.find_element(
        By.CSS_SELECTOR,
        "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)",
    )
    submit_button = driver.find_element(By.CSS_SELECTOR, ".Y5sE8d")

    address_input.send_keys(data["address"])
    price_input.send_keys(data["price"])
    link_input.send_keys(data["link"])
    submit_button.click()
    sleep(2)
