"""Sending Emails"""

"""
import os
from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage

### ------ CONFIG ------ ###

load_dotenv()
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))
USERNAME = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("SMTP_KEY")
SENDER_EMAIL = os.environ.get("EMAIL_FROM")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

msg = EmailMessage()
msg["Subject"] = "Hello from Python!"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg.set_content("This email was sent using Python.")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(USERNAME, PASSWORD)
    smtp.send_message(msg)

print("Email sent!")
"""


"""Working with datetime"""

import datetime

# print(datetime.datetime.now().second)

date = datetime.datetime(2026, 7, 8)
print(date)
