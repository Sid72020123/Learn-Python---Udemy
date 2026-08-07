from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    return f"<h3>Name: <i>{request.form['name']}</i></h3><h3>Password: <i>{request.form['password']}</i></h3>"


if __name__ == "__main__":
    app.run(debug=True)
