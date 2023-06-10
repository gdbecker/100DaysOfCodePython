# 100 Days of Code: Python
# May 4, 2022
# Treasure hunt "choose your own adventure" game!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to TREASURE ISLAND. Your mission is to find the treasure.")
inGame = True

# Part 1
if inGame == True:
    part1 = input("\nYou have arrived at a crossroads where Indiana Jones ran away from the boulder. Do you turn left or right? L/R: ")

if inGame == True and part1 == "L":
    inGame = True
elif inGame == True and part1 == "R":
    inGame = False
    print("Oh no! You fell into a hole. GAME OVER!")

# Part 2
if inGame == True:
    part2 = input("\nNow you are walking along the coastline and see a tidal wave coming from your left. Do you swim or wait? S/W: ")

if inGame == True and part2 == "W":
    inGame = True
if inGame == True and part2 == "S":
    inGame = False
    print("Sorry, you've been attacked by a school of trout! GAME OVER!")

# Part 3
if inGame == True:
    part3 = input("\nYou find yourself at a collection of three different colored doors floating in midair: red, yellow, and blue. Which door do you choose to walk through? R/Y/B: ")

if inGame == True and part3 == "Y":
    print("**CONGRATS!! You found the hidden treasure!!**")
elif inGame == True and part3 == "R":
    print("You walked into a room full of fire! GAME OVER!")
elif inGame == True and part3 == "B":
    print("You walked into a room full of beasts and were eaten. GAME OVER!")
