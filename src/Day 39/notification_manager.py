# Send Email
import os
import smtplib
from email.message import EmailMessage

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))
USERNAME = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("SMTP_KEY")
SENDER_EMAIL = os.environ.get("EMAIL_FROM")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")


def send_email_alert(flight):
    content = f"""Lowest Price alert for flight from {flight.departure_airport_id} [{flight.departure_time}] to {flight.arrival_airport_id} [{flight.arrival_time}]! Price: {flight.price}"""

    msg = EmailMessage()
    msg["Subject"] = "Cheap Flight Alert!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")
