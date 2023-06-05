# 100 Days of Code: Python
# May 5, 2022
# Reeborg World Maze problem
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    while right_is_clear():
        turn_right()
        move()
    while wall_on_right() and front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    if not front_is_clear() and not right_is_clear():
        turn_left()
