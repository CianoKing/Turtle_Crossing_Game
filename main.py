import random
from turtle import Screen
from car_manager import CarManager
import time
from player import Player
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Krissy Crossy")
screen.tracer(0)
scoreboard = ScoreBoard()
player = Player()
screen.setup(width=500, height=500)
screen.listen()
screen.onkeypress(key="Up", fun=player.move_player)
car_list = []
speed = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if random.randint(1, 6) == 3:
        cars = CarManager()
        car_list.append(cars)
        if len(car_list) > 1:
            if cars.distance(car_list[-2]) > 40:
                car_list.append(cars)
            else:
                car_list.remove(cars)

    for a_car in car_list:
        a_car.car_move(5 * speed)

    if player.ycor() > 230:
        speed = scoreboard.update_level()
        player.goto(0, -200)

    for car in car_list:
        if player.distance(car) < 24 and abs(abs(player.ycor())-abs(car.ycor())) < 22:
            print(player.distance(car))
            print(abs(abs(player.ycor())-abs(car.ycor())))
            game_is_on = False
            scoreboard.game_over()
            break

    screen.update()
screen. exitonclick()
