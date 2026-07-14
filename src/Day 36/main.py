import os
from dotenv import load_dotenv
from requests import get
import requests_cache

load_dotenv()

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "demo")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "demo")

STOCK = "TSLA"
COMPANY_NAME = "TESLA INC"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

requests_cache.install_cache("api_cache")


def get_time_series_stock_data():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    response = get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()

    stock_data = response.json()
    time_series_data = [value for _, value in stock_data["Time Series (Daily)"].items()]

    difference = abs(
        float(time_series_data[0]["4. close"]) - float(time_series_data[1]["4. close"])
    )

    difference_percent = (difference / float(time_series_data[0]["4. close"])) * 100
    print(f"Difference: {difference_percent:.2f} %\n\n")
    if difference_percent > 1:
        get_news()


def get_news():
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 10,
    }
    response = get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()

    articles = response.json()["articles"]
    print("=" * 25 + " News " + "=" * 25)
    for index, article in enumerate(articles):
        print(
            f"\t[{index + 1:02}] {article['author']}, {article['source']['name']}: {article['title']}\n"
        )


get_time_series_stock_data()
