"""
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()
"""

# Etch-a-Sketch Application

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.pensize(5)


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear_and_reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_and_reset)


screen.exitonclick()
