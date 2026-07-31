from flask import Flask

print(__name__)
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.get("/")
def hello_world():
    return "<h1 style='text-align: center;'>Hello World!</h1>"


@app.get("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.get("/username/<name>")
def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
