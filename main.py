import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

scoreboard = Scoreboard()

car_list = []
game_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.write_scoreboard(player.win_count)  # Level number display

    # Player movement
    screen.onkey(player.move, "Up")

    # Car spawn
    if game_count % 6 == 0:
        new_car = CarManager()
        car_list.append(new_car)
    for car in car_list:
        car.car_move(player.win_count)

        # Player collision with car
        if car.distance(player) < 17:
            scoreboard.game_over()
            game_is_on = False

    player.check_win()

    game_count += 1

screen.exitonclick()
