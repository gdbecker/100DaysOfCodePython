from turtle import Turtle
from missile import Missile

MOVE_DISTANCE = 20

class Ship(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color("blue")
        self.shape("triangle")
        self.shapesize(stretch_wid=3, stretch_len=1.5)
        self.setheading(90)
        self.penup()
        self.lives = 2
        self.goto(starting_position)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())