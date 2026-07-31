### --- Project 55 --- ###

from random import randint
from flask import Flask

print(__name__)
app = Flask(__name__)

NUMBER = randint(0, 9)


# def add_element(name):
#     def function_decorator(function):
#         def wrapper():
#             return f"<{name}>{function()}</{name}>"

#         return wrapper

#     return function_decorator

print(NUMBER)


@app.get("/")
# @add_element("h1")
def root():
    return "<h1>Guess a number between 0 and 9</h1><br><br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"


@app.get("/<int:n>")
def guess(n):
    if n == NUMBER:
        return "<h1 style='color: green;'>You found me!</h1><br><br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />"
    else:
        if n < NUMBER:
            return "<h1 style='color: red;'>Too low, try again!</h1><br><br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />"
        else:
            return "<h1 style='color: purple;'>Too high, try again!</h1><br><br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />"


if __name__ == "__main__":
    app.run(debug=True)
