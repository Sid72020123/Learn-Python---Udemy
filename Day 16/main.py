# --- OOP in Python ---

# Creating classes and objects

from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("green", "green")
t.forward(100)
s = Screen()
print(t, s)
s.exitonclick()
