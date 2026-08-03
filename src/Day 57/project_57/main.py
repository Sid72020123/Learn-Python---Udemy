from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route("/")
def home():
    response = get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    posts = response.json()

    return render_template("index.html", posts=posts)


@app.route("/post/<int:n>")
def get_post(n):
    response = get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()

    post = response.json()[n - 1]

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
