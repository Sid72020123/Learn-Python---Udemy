# --- Project 19 ---

# Turtles Race

from turtle import Turtle, Screen
from random import randint

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = [Turtle(shape="turtle") for _ in colors]
screen = Screen()
screen.setup(width=500, height=400)

user_bet = str(screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ",
)).strip().lower()

i = 0
for turtle in turtles:
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=-150 + 50 * i)
    i += 1

is_race_on = False
if user_bet:
    is_race_on = True

winning_color = ""
while is_race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230:  # 230 = 250 - (40 / 2)
            winning_color = turtle.pencolor()
            is_race_on = False
            break

if winning_color == user_bet:
    print(f"{winning_color.title()} turtle wins! You've won the bet!")
else:
    print(f"{winning_color.title()} turtle wins! You've lost the bet!")

screen.exitonclick()
