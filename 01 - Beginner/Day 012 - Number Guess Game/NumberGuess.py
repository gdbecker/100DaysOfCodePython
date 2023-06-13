# 100 Days of Code: Python
# May 10, 2022
# Number guessing game with the computer with easy/hard difficulty levels

import random
import os

# Set up game loop
keepGoing = True
logo = '''
 _______               ___.                    ________
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >
        \/            \/    \/     \/                \/            \/     \/     \/
'''

while keepGoing:
    print(logo)
    print("\n########## Welcome to the Number Guessing Game! ##########")
    print("I'm thinking of a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5

    number = random.randint(1,100)

    while lives > 0:
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < number:
            print("Too low.\nGuess again.")
            lives -= 1
        elif guess > number:
            print("Too high.\nGuess again.")
            lives -= 1
        elif guess == number:
            print("Congratualations! You got it!!")
            break

    if lives == 0 and guess != number:
        print("\nYou've run out of guesses, you lost.")

    ans = input("Would you like to play again? (Y/N) ")

    if ans == "Y":
        keepGoing = True
        os.system('cls')
    elif ans == "N":
        keepGoing = False
