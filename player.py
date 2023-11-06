from turtle import Turtle
STARTING_POSITION = (0, -200)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("forest green")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player(self):
        self.forward(10)

