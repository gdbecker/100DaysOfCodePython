from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 30

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.refresh()

    def refresh(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
