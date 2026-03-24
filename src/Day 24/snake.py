from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIR_UP = 90
DIR_DOWN = 270
DIR_RIGHT = 0
DIR_LEFT = 180


class Snake:
    def __init__(self) -> None:
        self.segments = []
        for position in STARTING_POSITIONS:
            self._create_snake_segment("square", "white", position)
        self.head = self.segments[0]

    def _create_snake_segment(self, shape, color, position):
        segment = Turtle(shape)
        segment.color(color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def increase_length(self):
        self._create_snake_segment("square", "white", self.segments[-1].position())

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIR_DOWN:
            self.head.setheading(DIR_UP)

    def down(self):
        if self.head.heading() != DIR_UP:
            self.head.setheading(DIR_DOWN)

    def left(self):
        if self.head.heading() != DIR_RIGHT:
            self.head.setheading(DIR_LEFT)

    def right(self):
        if self.head.heading() != DIR_LEFT:
            self.head.setheading(DIR_RIGHT)
