# 100 Days of Code: Python
# July 27-28, 2022
# GUI game: Space Invaders

# Import modules
from turtle import Turtle, Screen
from missile import Missile
from invader import Invader
from ship import Ship
from scoreboard import Scoreboard
import random
import time

# Static variables
MISSILE_HEADING_SHIP = 90
MISSILE_HEADING_INVADER = 270

# Starting variables
invaders = []
invader_missiles = []
ship_missiles = []
num_game_loops = 0

# Function for firing random invader missile
def fire_missile_invader():
    random_invader = random.choice(invaders[0])
    inv_x = random_invader.xcor()
    inv_y = random_invader.ycor()
    inv_missile = Missile(MISSILE_HEADING_INVADER)
    inv_missile.color("green")
    inv_missile.goto(inv_x, inv_y)
    invader_missiles.append(inv_missile)

# Function for firing ship missile
def fire_missile_ship():
    ship_x = main_ship.xcor()
    ship_y = main_ship.ycor()
    ship_missile = Missile(MISSILE_HEADING_SHIP)
    ship_missile.color("blue")
    ship_missile.goto(ship_x, ship_y)
    ship_missiles.append(ship_missile)

# Set up the screen
screen = Screen()
screen.setup(width=600, height=700)
# screen.colormode(255)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

# Make invaders and ship
num_in_row = 7
y_cor = 230
x_cor = -200
for row in range(3):
    invaders_in_row = []
    for numInvader in range(num_in_row):
        i = Invader((x_cor, y_cor))
        invaders_in_row.append(i)
        x_cor += 62
    invaders.append(invaders_in_row)
    x_cor = -200
    y_cor += 40

main_ship = Ship((0, -270))

# Draw line at bottom of screen
bottom = Turtle()
bottom.color("blue")
bottom.pensize(2)
bottom.setheading(0)
bottom.penup()
bottom.goto((-280, -295))
for l in range(27):
    bottom.pendown()
    bottom.forward(20)
bottom.hideturtle()

# Setup scoreboard
scoreboard = Scoreboard((-190, -330))

# Start listening to up/down keys depending on the main ship
screen.listen()
screen.onkeypress(main_ship.move_left, "Left")
screen.onkeypress(main_ship.move_right, "Right")
screen.onkeypress(fire_missile_ship, "space")

# Game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Control each invader movement
    for invader_row in invaders:
        for inv in invader_row:
            if inv.mode == 0:
                inv.move_left()
            elif inv.mode == 1:
                inv.move_right()

    # Control random invader missile firing
    if num_game_loops % 10 == 0:
        fire_missile_invader()

    # Move all invader missiles
    for im in invader_missiles:
        im.move()

    # Move all ship missiles
    for sm in ship_missiles:
        sm.move()

    # Detect if ship missile hits an invader
    for invader_row in invaders:
        for inv in invader_row:
            for sm in ship_missiles:
                if sm.distance(inv) < 21:
                    invader_row.remove(inv)
                    inv.goto(500,500)
                    sm.goto(500,500)

    # Detect if invader missile hits the ship
    for im in invader_missiles:
        if im.distance(main_ship) < 20:
            main_ship.goto((0, -270))
            scoreboard.decrease_lives()
            scoreboard.update_scoreboard()

    # Remove empty lists of invaders from overall invaders container
    for invader_row in invaders:
        if len(invader_row) == 0:
            invaders.remove(invader_row)

    # Detect when invaders switch direction
    # Left to Right
    invaders_screen_left = False
    for invader_row in invaders:
        if invader_row[0].xcor() <= -280:
            invaders_screen_left = True

    if invaders_screen_left:
        for invader_row in invaders:
            for inv in invader_row:
                inv.mode = 1

    # Right to Left
    invaders_screen_right = False
    for invader_row in invaders:
        if invader_row[-1].xcor() >= 280:
            invaders_screen_right = True

    if invaders_screen_right:
        for invader_row in invaders:
            for inv in invader_row:
                inv.mode = 0

    # Detect when game is won
    if len(invaders) == 0:
        scoreboard.game_won()
        game_is_on = False

    # Detect when ship lost all lives
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    num_game_loops += 1

# Ending screen controls
screen.exitonclick()