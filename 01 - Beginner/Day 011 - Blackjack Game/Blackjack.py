# 100 Days of Code: Python
# May 9, 2022
# Blackjack capstone project
# Play Blackjack with the computer

import random
import os

# Function to create a card deck
def makeDeck():
    """
    Makes a brand new deck of cards
    """

    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    deck = {}

    for suit in suits:
        for face in faces:
            cardName = face + " of " + suit

            if face == "Jack" or face == "Queen" or face == "King":
                deck[cardName] = 10
            else:
                deck[cardName] = faces.index(face) + 1

    return deck

# Set up variables and game loop
keepGoing = True
logo = '''
                                  _____
                          _____  |K  WW|
                  _____  |Q  ww| | /\{)|          _     _            _    _            _
           _____ |J  ww| | /\{(| | \/%%| _____   | |   | |          | |  (_)          | |
          |10 o || /\{)| | \/%%| |  %%%||A ^  |  | |__ | | __ _  ___| | ___  __ _  ___| | __
          |o o o|| \/% | |  %%%| |_%%%>|| / \ |  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
          |o o o||   % | |_%%%O|        | \ / |  | |_) | | (_| | (__|   <| | (_| | (__|   <
          |o o o||__%%[|                |  .  |  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
          |___0I|                       |____V|                         _/ |
                                                                       |__/
'''

while keepGoing:
    answer = input("\nDo you want to play Blackjack? (y/n) ")

    if answer == "y":
        keepGoing = True
    elif answer == "n":
        keepGoing = False
        break

    os.system('cls')
    print(logo)

    # Set up deck, variables, and initial player/comp cards
    inGame = True
    deckDict = makeDeck()
    deckList = list(deckDict.keys())
    random.shuffle(deckList)

    playerCards = []
    playerCards.append(deckList.pop())
    playerCards.append(deckList.pop())

    compCards = []
    compCards.append(deckList.pop())
    compCards.append(deckList.pop())

    ans = "y"

    while inGame:
        playerScore = 0
        for pCard in playerCards:
            playerScore += deckDict[pCard]

        compScore = 0
        for cCard in compCards:
            compScore += deckDict[cCard]

        if playerScore <= 21 and compScore <= 21 and playerScore == compScore:
            print(f"\nYour final hand: {playerCards} -> Final Score: {playerScore}")
            print(f"Computer's final hand: {compCards} -> Final Score: {compScore}")
            print("It's a draw!")
            inGame = False
            break
        elif playerScore <= 21 and compScore <= 21 and ans == "y":
            print(f"\nYour cards: {playerCards} -> Current Score: {playerScore}")
            print(f"Computer's first card: {compCards[0]}")
            inGame = True
        elif playerScore <= 21 and compScore <= 21 and ans == "n" and compScore > playerScore:
            print(f"\nYour final hand: {playerCards} -> Final Score: {playerScore}")
            print(f"Computer's final hand: {compCards} -> Final Score: {compScore}")
            print("Sorry you lost!")
            inGame = False
            break
        elif playerScore <= 21 and compScore <= 21 and ans == "n" and compScore < playerScore:
            print(f"\nYour final hand: {playerCards} -> Final Score: {playerScore}")
            print(f"Computer's final hand: {compCards} -> Final Score: {compScore}")
            print("You won!")
            inGame = False
            break
        elif playerScore > 21 and compScore <=21:
            print(f"\nYour final hand: {playerCards} -> Final Score: {playerScore}")
            print(f"Computer's final hand: {compCards} -> Final Score: {compScore}")
            print("You went over, sorry you lost!")
            inGame = False
            break
        elif playerScore <= 21 and compScore > 21:
            print(f"\nYour final hand: {playerCards} -> Final Score: {playerScore}")
            print(f"Computer's final hand: {compCards} -> Final Score: {compScore}")
            print("Computer went over! You win!")
            inGame = False
            break

        ans = input("\nHit or pass? ('y' for hit/'n' for pass) ")

        if ans == "y":
            playerCards.append(deckList.pop())

            if compScore <= 17:
                compCards.append(deckList.pop())
        elif ans == "n":
            while compScore <= 17:
                newCompCard = deckList.pop()
                compCards.append(newCompCard)
                compScore += deckDict[newCompCard]
