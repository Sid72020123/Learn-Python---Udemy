# --- Project 18 ---

from json import loads, dumps
from random import choice
from turtle import Turtle, Screen
import colorgram

turtle = Turtle()
screen = Screen()

turtle.speed(0)
turtle.hideturtle()
turtle.pensize(20)
screen.colormode(255)

width, height = screen.screensize()

EXTRACT_COLORS = False

if EXTRACT_COLORS:
    colors = colorgram.extract("image.jpg", 10)

    extracted_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        extracted_colors.append((r, g, b))

    with open("extracted.json", "w+") as file:
        file.write(dumps(extracted_colors))

extracted_colors = []
with open("extracted.json", "r") as file:
    extracted_colors = loads(file.read())

turtle.penup()
turtle.goto(-width // 2, -height // 2)
for _ in range(10):
    for _ in range(10):
        turtle.dot(20, choice(extracted_colors))
        turtle.forward(50)
    turtle.goto(-width // 2, turtle.pos()[1] + 50)

screen.exitonclick()
