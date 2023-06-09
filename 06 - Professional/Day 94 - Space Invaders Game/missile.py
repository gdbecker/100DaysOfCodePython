from turtle import Turtle

STARTING_SPEED = 4
MOVE_DISTANCE = 18

class Missile(Turtle):
    def __init__(self, heading):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=1.5)
        self.penup()
        self.rate = STARTING_SPEED
        self.speed(self.rate)
        self.setheading(heading)

    def move(self):
        self.forward(MOVE_DISTANCE)