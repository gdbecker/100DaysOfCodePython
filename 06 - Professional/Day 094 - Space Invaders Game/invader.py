from turtle import Turtle

MOVE_DISTANCE = 7
LEFT = 180
RIGHT = 0

class Invader(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.shapesize(stretch_wid=1.3, stretch_len=1.3)
        self.setheading(270)
        self.penup()
        self.mode = 0
        self.goto(starting_position)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

