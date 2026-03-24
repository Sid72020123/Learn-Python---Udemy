import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
cm = CarManager()
s = Scoreboard()

screen.listen()
screen.onkeypress(p.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cm.create_car()
    cm.move_cars()

    # Detection collision with cars
    for car in cm.all_cars:
        if car.distance(p) < 20:
            game_is_on = False
            s.display_game_over()

    # Detect a successful crossing
    if p.is_at_finish_line():
        p.go_to_start()
        cm.level_up()
        s.increase_level()

screen.exitonclick()
