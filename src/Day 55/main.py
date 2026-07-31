# from flask import Flask

# print(__name__)
# app = Flask(__name__)


# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"

#     return wrapper


# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"

#     return wrapper


# def make_underline(function):
#     def wrapper():
#         return f"<u>{function()}</u>"

#     return wrapper


# @app.get("/")
# def hello_world():
#     return "<h1 style='text-align: center;'>Hello World!</h1>"


# @app.get("/bye")
# @make_bold
# @make_emphasis
# @make_underline
# def bye():
#     return "Bye!"


# @app.get("/username/<name>")
# def greet(name):
#     return f"Hello, {name}!"


# if __name__ == "__main__":
#     app.run(debug=True)


### --- Coding Exercise 23: Advanced Decorators ---
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {func(*args)}")
        return func(*args)

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


print(a_function(1, 4, 10))
