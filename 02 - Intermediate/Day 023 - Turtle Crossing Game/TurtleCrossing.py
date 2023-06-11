# 100 Days of Code: Python
# May 17, 2022
# Turtle Crossing game

# Import modules
from turtle import Turtle, Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time
import random

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

# Make main player turtle
main = Player()

# Make cars
cars = []
num_in_row = 1
y_cor = -240
for row in range(16):
    for numCar in range(num_in_row):
        cars_in_row = []
        c = Car((random.randint(-300, 300), y_cor))
        cars_in_row.append(c)
    cars.extend(cars_in_row)
    y_cor += 30

# Make level tracker scoreboard
level_scoreboard = Scoreboard((-190, 240))

# Start listening to up key for moving the turtle
screen.listen()
screen.onkey(main.move, "Up")

# Game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for c in cars:
        c.move()

    # Detect collision with a car
    for c in cars:
        if main.distance(c) < 18:
            level_scoreboard.game_over()
            game_is_on = False

    # Detect reaching next level
    if main.ycor() >= 280:
        level_scoreboard.level_up()
        main.refresh()
        for c in cars:
            c.increase_speed()

# Ending screen controls
screen.exitonclick()