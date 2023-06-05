# 100 Days of Code: Python
# May 4, 2022
# Play Rock, Paper, Scissors against the computer

import random

move = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
comp = random.randint(0,2)

# Show your move
if move == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif move == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif move == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

# Show computer move
print("Computer chose:\n")
if comp == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif comp == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif comp == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

# Decide winner
if move == comp:
    print("\nIt's a tie!")
if (move == 0 and comp == 2) or (move == 1 and comp == 0) or (move == 2 and comp == 1):
    print("CONGRATS you won!")
elif (comp == 0 and move == 2) or (comp == 1 and move == 0) or (comp == 2 and move == 1):
    print("Sorry, Computer won.")
