from requests import get
from flask import Flask, render_template, request

app = Flask(__name__)


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
        return "<h1>Form Submitted Successfully!</h1>"
    else:
        return "Invalid request method!"


if __name__ == "__main__":
    app.run(debug=True)
