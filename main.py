import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()