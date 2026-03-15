# Python Turtle

from random import randint, choice
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# turtle.shape("turtle")
# turtle.color("red")
turtle.pensize(5)
turtle.speed(0)


def reset():
    screen.clearscreen()
    turtle.home()
    screen.colormode(255)


# Challenge 1
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

reset()

# Challenge 2
for _ in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

reset()

# Challenge 3
for sides in range(3, 11):
    turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)

reset()

# Challenge 4
for _ in range(200):
    turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.forward(30)
    turtle.right(choice([0, 90, 180, 270]))

reset()


# Challenge 5: Spirograph
def draw_spirograph(size_of_gap=5):
    turtle.pensize(2)
    for _ in range(int(360 / size_of_gap)):
        turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        turtle.right(5)
        turtle.circle(150)


draw_spirograph()

screen.exitonclick()
