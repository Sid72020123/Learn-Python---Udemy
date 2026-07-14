import os
from dotenv import load_dotenv
from requests import get
import requests_cache

load_dotenv()

ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "demo")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "demo")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

requests_cache.install_cache("api_cache")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


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
    print(difference_percent)
    if difference_percent > 5:
        print("Get News")
    get_news()


def get_news():
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 5,
    }
    response = get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()

    print(response.json())


get_time_series_stock_data()
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
