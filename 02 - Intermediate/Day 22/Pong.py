# 100 Days of Code: Python
# May 16, 2022
# Classic Pong game

# Import modules
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

# Heading direction static variables
BALL_HEADINGS = [45, 135, 225, 315]

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Dashed line in middle of screen
middle = Turtle()
middle.color("white")
middle.pensize(3)
middle.setheading(90)
middle.penup()
middle.goto((0, -400))
for l in range(20):
    middle.pendown()
    middle.forward(20)
    middle.penup()
    middle.forward(20)

# Make paddles, ball, and scoreboards
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_scoreboard = Scoreboard((70, 220))
left_scoreboard = Scoreboard((-70, 220))

# Start listening to up/down keys depending on the paddle
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Game loop
game_is_on = True
ball.setheading(random.choice(BALL_HEADINGS))

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with top/bottom
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_top_bottom()

    # Detect collision with a paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    # Detect if paddle misses the ball
    if ball.xcor() >= 400:
        left_scoreboard.increase_score()
        ball.refresh()
        ball.setheading(random.choice(BALL_HEADINGS))
        ball.increase_speed()
    elif ball.xcor() <= -400:
        right_scoreboard.increase_score()
        ball.refresh()
        ball.setheading(random.choice(BALL_HEADINGS))
        ball.increase_speed()

# Ending screen controls
screen.exitonclick()