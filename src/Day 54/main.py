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
from random import randint


def decorator_function(function):
    print(f"I'm inside decorator function. Argument passed: {function}")

    def wrapper_function():
        delay = randint(1, 5)
        print(f"Delaying for {delay} seconds...")
        sleep(delay)
        print("Calling the passed function...")
        function()

    return wrapper_function


@decorator_function
def say_hello():
    print("Hello!")


@decorator_function
def say_bye():
    print("Bye!")


@decorator_function
def say_greeting():
    print("How are you?")


say_hello()


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
