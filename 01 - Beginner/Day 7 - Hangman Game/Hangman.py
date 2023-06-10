# 100 Days of Code: Python
# May 6, 2022
# Play Hangman with the computer

import random
import os

# Function to grab hangman diagram based on number of lives
def getPic(livesLeft):
    if livesLeft == 0:
        print('''\n
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / |
             |
         ____|___
        ''')
    elif livesLeft == 1:
        print('''\n
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      /
             |
         ____|___
        ''')
    elif livesLeft == 2:
        print('''\n
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |
             |
         ____|___
        ''')
    elif livesLeft == 3:
        print('''\n
              _______
             |/      |
             |      (_)
             |      \|/
             |
             |
             |
         ____|___
        ''')
    elif livesLeft == 4:
        print('''\n
              _______
             |/      |
             |      (_)
             |      \|
             |
             |
             |
         ____|___
        ''')
    elif livesLeft == 5:
        print('''\n
              _______
             |/      |
             |      (_)
             |       |
             |
             |
             |
         ____|___
        ''')
    elif livesLeft == 6:
        print('''\n
              _______
             |/      |
             |      (_)
             |
             |
             |
             |
         ____|___
        ''')

# Function to check if they guessed the word
def checkGuess(guessWord):
    guessComplete = True
    for letter in guessWord:
        if letter == "_":
            guessComplete = False
            break

    return guessComplete

# Word list
words = ["banana", "discover", "spaceship", "monkey", "zebra", "skyscraper", "birdwatcher", "tundra", "ultimate", "costume"]

# Generate a random word & set up user's guess
gameWord = words[random.randint(0,len(words) - 1)]
gameWord = list(gameWord)
guessWord = []
for spot in range(0,len(gameWord)):
    guessWord.append("_")

# Loop while game is not over
print('''
88
88
88
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba,
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88
                                    aa,    ,88
                                     "Y8bbdP"
==========================================================================================\n
''')

gameOver = False
numLives = 7

while not gameOver:
    correctGuess = False
    guess = input("Guess a letter: ")

    for index in range(0,len(gameWord)):
        if gameWord[index] == guess and guessWord[index] == "_":
            correctGuess = True
            guessWord[index] = guess
            continue

    os.system('cls')

    if not correctGuess:
        numLives -= 1
        getPic(numLives)
        print(f"You guessed {guess}, that's not in the word. You lost a life.")

    print(' '.join(guessWord) + "\n")
    guessComplete = checkGuess(guessWord)

    if guessComplete and numLives > 0:
        print("YOU WON THE GAME CONGRATS!!")
        gameOver = True

    if not guessComplete and numLives == 0:
        print("Sorry you lost!")
        gameOver = True
