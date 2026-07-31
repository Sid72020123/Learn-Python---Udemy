from flask import Flask

print(__name__)
app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<h1>Hello World!</h1>"


@app.get("/bye")
def bye():
    return "Bye!"


@app.get("/username/<name>")
def greet(name):
    return f"Hello, {name + 12}!"


if __name__ == "__main__":
    app.run(debug=True)
