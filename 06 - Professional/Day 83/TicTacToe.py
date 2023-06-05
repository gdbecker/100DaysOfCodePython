# 100 Days of Code: Python
# July 7, 2022
# Tic Tac Toe game

# Import modules
import random
import os

# Initial variables
in_app = True
game_active = True
board_moves = {
    "1":" ",
    "2":" ",
    "3":" ",
    "4":" ",
    "5":" ",
    "6":" ",
    "7":" ",
    "8":" ",
    "9":" "
}

# Get game started
while in_app:
    print("xoxoxoxoxo WELCOME TO TIC TAC TOE xoxoxoxoxo")
    player_icon = input("\nWould you like to be X's or O's? ").upper()
    if player_icon == "X":
        comp_icon = "O"
    else:
        comp_icon = "X"

    # Active gameplay
    while game_active:
        print(f'''
            Board Ref:              {board_moves["1"]} | {board_moves["2"]} | {board_moves["3"]}  
            1 | 2 | 3              -----------
            4 | 5 | 6               {board_moves["4"]} | {board_moves["5"]} | {board_moves["6"]} 
            7 | 8 | 9              -----------
                                    {board_moves["7"]} | {board_moves["8"]} | {board_moves["9"]} 
        ''')

        player_move = str(input("Make your move: "))
        board_moves[player_move] = player_icon
        comp_move = random.choice(list(board_moves))

        # Make sure computer picks a blank spot
        while board_moves[comp_move] != " ":
            comp_move = random.choice(list(board_moves))
        board_moves[comp_move] = comp_icon

        # Check for winning status
        if (board_moves["1"] == board_moves["2"] == board_moves["3"] == player_icon) or \
            (board_moves["4"] == board_moves["5"] == board_moves["6"] == player_icon) or \
            (board_moves["7"] == board_moves["8"] == board_moves["9"] == player_icon) or \
            (board_moves["1"] == board_moves["4"] == board_moves["7"] == player_icon) or \
            (board_moves["2"] == board_moves["5"] == board_moves["8"] == player_icon) or \
            (board_moves["3"] == board_moves["6"] == board_moves["9"] == player_icon) or \
            (board_moves["1"] == board_moves["5"] == board_moves["9"] == player_icon) or \
            (board_moves["3"] == board_moves["5"] == board_moves["7"] == player_icon):
            game_active = False
            print("\n*** YOU WON CONGRATS! ***")
        elif (board_moves["1"] == board_moves["2"] == board_moves["3"] == comp_move) or \
            (board_moves["4"] == board_moves["5"] == board_moves["6"] == comp_move) or \
            (board_moves["7"] == board_moves["8"] == board_moves["9"] == comp_move) or \
            (board_moves["1"] == board_moves["4"] == board_moves["7"] == comp_move) or \
            (board_moves["2"] == board_moves["5"] == board_moves["8"] == comp_move) or \
            (board_moves["3"] == board_moves["6"] == board_moves["9"] == comp_move) or \
            (board_moves["1"] == board_moves["5"] == board_moves["9"] == comp_move) or \
            (board_moves["3"] == board_moves["5"] == board_moves["7"] == comp_move):
            game_active = False
            print("\nComputer won :(")
        elif board_moves["1"] != " " and board_moves["2"] != " " and board_moves["3"] != " " and \
            board_moves["4"] != " " and board_moves["5"] != " " and board_moves["6"] != " " and \
            board_moves["7"] != " " and board_moves["8"] != " " and board_moves["9"] != " ":
            game_active = False
            print("\nDRAW")
        os.system('cls')

    player_ans = input("\nWould you like to play again? (Y/N) ").upper()

    if player_ans == "N":
        in_app = False
    else:
        board_moves = {
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " "
        }

    os.system('cls')