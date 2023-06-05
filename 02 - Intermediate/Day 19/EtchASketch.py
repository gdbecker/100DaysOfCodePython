# 100 Days of Code: Python
# May 14, 2022
# Etch-A-Sketch app with Turtle class

# Import modules
from turtle import Turtle, Screen

# Set up main variables
sam = Turtle()
screen = Screen()

# Function for moving the turtle forward
def move_forwards():
    sam.forward(15)

# Function for moving the turtle backwards
def move_backwards():
    sam.backward(15)

# Functions for changing turtle direction heading
def turn_counter_clockwise():
    new_heading = sam.heading() - 5
    sam.setheading(new_heading)

def turn_clockwise():
    new_heading = sam.heading() + 5
    sam.setheading(new_heading)

# Function for resetting the screen
def reset_screen():
    sam.penup()
    sam.goto(0,0)
    sam.clear()
    sam.pendown()

# Set up the screen for 'listening' to key inputs
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=reset_screen)

# Ending screen controls
screen.exitonclick()