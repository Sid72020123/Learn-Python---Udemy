from flask import Flask, render_template
from random import randint
from datetime import datetime
from requests import get

app = Flask(__name__)


@app.get("/")
def root():
    return render_template(
        "index.html", number=randint(10, 99), copyright=datetime.now().year
    )


@app.get("/guess/<name>")
def guess_name(name):
    gender_response = get("https://api.genderize.io", params={"name": name})
    age_response = get("https://api.agify.io", params={"name": name})
    gender_response.raise_for_status()
    age_response.raise_for_status()

    gender_data = gender_response.json()
    age_data = age_response.json()

    gender = gender_data["gender"]
    age = age_data["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.get("/blog/<num>")
def get_blog(num):
    response = get("https://api.npoint.io/c790b4d5cab58020d391")

    data = response.json()

    return render_template("blog.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
