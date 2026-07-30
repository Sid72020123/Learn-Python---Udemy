# from flask import Flask

# print(__name__)
# app = Flask(__name__)


# @app.get("/")
# def hello_world():
#     return "Hello World!"


# if __name__ == "__main__":
#     app.run()

# ==> Nested functions in Python
# def outer_func():
#     print("I'm outer")

#     def inner_func():
#         print("I'm inner")

#     return inner_func

# outer_func()()


# Python Decorator Function

from time import sleep


def decorator_factory(delay):
    print(f"I'm inside the decorator factory. Argument passed: {delay}")

    def decorator_function(function):
        print(f"I'm inside decorator function. Argument passed: {function}")

        def wrapper_function():
            print(f"Delaying for {delay} seconds...")
            sleep(delay)
            print("Calling the passed function...")
            function()

        return wrapper_function

    return decorator_function


@decorator_factory(3)
def say_hello():
    print("Hello!")


@decorator_factory(2)
def say_bye():
    print("Bye!")


@decorator_factory(5)
def say_greeting():
    print("How are you?")


say_hello()
say_greeting()
say_bye()


"""
# --- Coding Exercise 22 ---
import time

# Write your code below 👇

print(time.time())


def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
"""
