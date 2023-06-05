from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.set_color()
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.setheading(180)
        self.rate = 2
        self.speed(self.rate)
        self.goto(position)

    # Function for making a random color
    def set_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        self.color(r, g, b)

    def move(self):
        self.forward(20)
        y_cor = self.ycor()
        if self.xcor() <= -360:
            self.goto(360, y_cor)

    def increase_speed(self):
        self.rate += 0.5
        self.speed(self.rate)
