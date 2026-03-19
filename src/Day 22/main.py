# Pong Game

import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turn off screen updates
screen.delay(0)

left_paddle = Paddle()
right_paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()

left_paddle.set_position(-350, 0)
right_paddle.set_position(350, 0)

screen.listen()  # Start listening for events
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top & bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(left_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
