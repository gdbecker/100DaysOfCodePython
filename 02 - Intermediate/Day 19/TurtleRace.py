# 100 Days of Code: Python
# May 14, 2022
# Race of the turtles!!

# Import modules
from turtle import Turtle, Screen
import random

# Set up the screen and turtles for racing
screen = Screen()
screen.setup(500,400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -90

all_turtles = []

for col in colors:
    t = Turtle(shape="turtle")
    t.color(col)
    t.penup()
    t.goto(-230,y)
    y += 40
    all_turtles.append(t)

step_sizes = [1, 3, 5, 7, 9, 11, 13, 15]

# Race loop
guess = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win? Enter a color: ")
is_at_end = False

while not is_at_end:
    for turtle in all_turtles:
        turtle.forward(random.choice(step_sizes))

        if turtle.xcor() >= 230:
            winning_turtle = turtle
            is_at_end = True
            break

# Print race results
winning_color = winning_turtle.color()[0]

if guess == winning_color:
    print(f"Congrats!! You guessed right! The winner is {winning_color}!")
else:
    print(f"Sorry, you guessed wrong. The winner is {winning_color}.")

# Ending screen controls
screen.exitonclick()