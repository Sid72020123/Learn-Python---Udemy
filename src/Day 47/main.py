import os
import smtplib
from email.message import EmailMessage

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from requests import get

URL = "https://appbrewery.github.io/instant_pot/"
load_dotenv()
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))
USERNAME = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("SMTP_KEY")
SENDER_EMAIL = os.environ.get("EMAIL_FROM")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

MIN_PRICE_LIMIT = 100


def send_email(price):
    content = f"""Low price alert for product!\nThe price today is {price}!"""

    msg = EmailMessage()
    msg["Subject"] = "Product Price Alert!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")


response = get(
    URL,
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.3 Safari/537.36"
    },
)

if response.status_code != 200:
    print("Failed to fetch the website:", response)

content = response.content

soup = BeautifulSoup(content, "html.parser")

price = float(soup.find("span", class_="a-offscreen").get_text().split("$")[1])

print("Product Price:", price)

if price <= MIN_PRICE_LIMIT:
    send_email(price)
