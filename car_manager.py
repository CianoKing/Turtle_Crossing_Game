from turtle import Turtle, Screen
import random
COLOURS = ["red", "yellow", "green", "blue", "orange", "purple"]
MOVE_SPEED = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car()

    def car(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3)
        self.color(random.choice(COLOURS))
        car_y = 20 * random.randint(-8, 8)
        self.goto(300, car_y)

    def car_move(self, speed):
        self.backward(speed)


