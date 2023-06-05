# 100 Days of Code: Python
# May 13, 2022
# Create random dot artwork with Turtle package

# Import modules
import turtle
from turtle import Turtle, Screen
import random
import colorgram

# Get color palette for painting
colorsRaw = colorgram.extract("image.jpg", 10)
colorsList = []
for c in colorsRaw:
    r = c.rgb[0]
    g = c.rgb[1]
    b = c.rgb[2]
    col = (r, g, b)
    colorsList.append(col)

# Set up screen
screen = Screen()
screen.colormode(255)

# Get the turtle going
timmy = Turtle()
timmy.shape("classic")
timmy.speed(10)
timmy.penup()

x = -200
y = -200

timmy.goto(x, y)
for x in range(10):
    for y in range(10):
        timmy.dot(20, random.choice(colorsList))
        timmy.forward(50)
    timmy.backward(10*50)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
timmy.hideturtle()

# Ending screen controls
screen.exitonclick()
