from turtle import Turtle

PADDLE_WIDTH = 80
PADDLE_HEIGHT = 100


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=PADDLE_HEIGHT // 20)
        self.penup()
        self.x_pos = 0
        self.y_pos = 0

    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            self.set_position(self.x_pos, self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.set_position(self.x_pos, self.ycor() - 20)
