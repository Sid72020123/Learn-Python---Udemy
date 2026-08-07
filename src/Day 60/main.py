import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

from requests import get
from flask import Flask, render_template, request

load_dotenv()

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "00000"))
USERNAME = os.environ.get("EMAIL_USERNAME")
PASSWORD = os.environ.get("SMTP_KEY")
SENDER_EMAIL = os.environ.get("EMAIL_FROM")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")

app = Flask(__name__)


def send_email(data):
    content = f"""Name: {data['name']}\nEmail: {data['email']}\nPhone Number: {data['phone']}\n\nMessage: {data['message']}"""

    msg = EmailMessage()
    msg["Subject"] = "New Message from Blog Contact!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(USERNAME, PASSWORD)
        smtp.send_message(msg)

    print("Email sent!")


def get_posts():
    response = get("https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()

    return response.json()


@app.get("/")
def root():
    return render_template("index.html", posts=get_posts())


@app.get("/post/<int:n>")
def post(n):
    post_content = get_posts()[n - 1]
    return render_template("post.html", post_content=post_content)


@app.get("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        data = request.form
        send_email(data)
        return "<h1>Form Submitted Successfully!</h1>"
    else:
        return "Invalid request method!"


if __name__ == "__main__":
    app.run(debug=True)
