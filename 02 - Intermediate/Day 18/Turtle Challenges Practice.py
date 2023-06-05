# Import Turtle modules & any other modules
from turtle import Turtle, Screen
import random

# Make a Turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# Screen controls start
screen = Screen()
screen.colormode(255)

# Challenge 1: draw a square
# for a in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Challenge 2: draw a dashed line
# for b in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Challenge 3: draw series of shapes from square to decagon - random color for each shape
# colors = ["red", "beige", "coral", "aquamarine", "DarkOrchid", "DarkOrange", "DeepPink", "DarkGreen", "blue", "BlueViolet"]
# for c in range(4,11):
#     angle = 360/c
#     timmy.color(random.choice(colors))
#     for c_sub in range(0,c):
#         timmy.forward(100)
#         timmy.right(angle)

# Challenge 4: generate a random walk
# colors = ["red", "beige", "coral", "aquamarine", "DarkOrchid", "DarkOrange", "DeepPink", "DarkGreen", "blue", "BlueViolet"]
# directions = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed(10)
#
# for d in range(101):
#     timmy.color(random.choice(colors))
#     direction = random.randint(1, 4)
#     timmy.right(random.choice(directions))
#     timmy.forward(25)

# Generate a random color with RGB values
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Challenge 5: draw a spirograph
# timmy.speed(0)

# for e in range(int(360 / 5)):
#     timmy.color(random_color())
#     timmy.circle(50)
#     timmy.left(5)

# Turn into a spirograph function
def draw_spirograph(circle_size, circle_density):
    for e in range(int(360 / circle_density)):
        timmy.color(random_color())
        timmy.circle(circle_size)
        timmy.left(circle_density)

# draw_spirograph(150, 6)

# Screen controls
screen.exitonclick()