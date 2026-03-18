from random import randrange
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.teleport_to_random_location()

    def teleport_to_random_location(self):
        self.goto(randrange(-280, 280, 10), randrange(-280, 280, 10))
