# 100 Days of Code: Python
# July 10-11, 2022
# GUI game: Breakout

# Import modules
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import random
import time

# Heading direction static variables
BALL_HEADINGS_START = [45, 135]

# Set up the screen
screen = Screen()
screen.setup(width=600, height=700)
# screen.colormode(255)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

# Make paddle, ball, walls, and scoreboard
main_paddle = Paddle((0, -310))
ball = Ball()

walls = []
num_in_row = 9
y_cor = 120
x_cor = -250
for row in range(6):
    walls_in_row = []
    for numWall in range(num_in_row):
        w = Wall((x_cor, y_cor))
        if row == 0 or row == 1:
            w.color("yellow")
        elif row == 2 or row == 3:
            w.color("orange")
        elif row == 4 or row == 5:
            w.color("red")
        walls_in_row.append(w)
        x_cor += 62
    walls.extend(walls_in_row)
    x_cor = -250
    y_cor += 30

num_walls_left = len(walls)

scoreboard = Scoreboard((0, 290), num_walls_left)

# Start listening to up/down keys depending on the paddle
screen.listen()
screen.onkey(main_paddle.move_left, "Left")
screen.onkey(main_paddle.move_right, "Right")

# Game loop
game_is_on = True
ball.setheading(random.choice(BALL_HEADINGS_START))

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with left/right
    if ball.xcor() >= 280 or ball.xcor() <= -280:
        ball.bounce_left_right()

    # Detect collision with the paddle
    if ball.distance(main_paddle) < 50 and ball.ycor() < -290:
        ball.bounce_up_down()

    # Detect collision with the top
    if ball.ycor() > 290:
        ball.bounce_up_down()

    # Detect collision with a wall
    for w in walls:
        if ball.distance(w) < 21:
            walls.remove(w)
            num_walls_left = len(walls)
            w.goto(500,500)
            ball.bounce_up_down()
            scoreboard.increase_score(num_walls_left)

    # Detect if paddle misses ball
    if ball.ycor() < -320:
        game_is_on = False
        scoreboard.game_over()

    # Detect if all walls are gone
    if len(walls) == 0:
        game_is_on = False
        scoreboard.game_won()

# Ending screen controls
screen.exitonclick()