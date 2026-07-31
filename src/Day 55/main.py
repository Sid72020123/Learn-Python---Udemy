from flask import Flask

print(__name__)
app = Flask(__name__)


@app.get("/")
def hello_world():
    return "Hello World!"


@app.get("/bye")
def bye():
    return "Bye!"


@app.get("/username/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run()
