# 100 Days of Code: Python
# May 8, 2022
# Multiple people input bids, prints out who won the auction

import os

# Function to add a bid
def addBid(bidDict, name, amt):
    bidDict[name] = amt
    return bidDict

# Function to get auction winner
def highestBidder(bidDict):
    winner = ""
    maxValue = 0

    for key, value in bidDict.items():
        if value > maxValue:
            winner = key
            maxValue = value

    return {"winner": winner, "amt": maxValue}

# Set up variables and Loop
keepGoing = True
bids = {}
winner = {}

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
print("--- Welcome to the Silent Auction! ---")

while keepGoing:
    name = input("\nWhat is your name? ")
    amt = int(input("\nWhat's your bid? $"))

    bids = addBid(bids, name, amt)

    answer = input("\nAre there any other bidders? Type 'yes' or 'no': ")

    if answer == "no":
        winner = highestBidder(bids)
        keepGoing = False
    elif answer == "yes":
        keepGoing = True

    os.system('cls')

# Print results
winnerName = winner["winner"]
winnerAmt = winner["amt"]

print(f"The winner is {winnerName} with amount ${winnerAmt}!")
