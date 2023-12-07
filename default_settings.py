"""
When initiate game, makes a map and a character.
"""

import random


# how to print grid map
def make_board():

    room_values = ["Lush Veshok Tree Forests", "The Armorer's Space", "Shipyards",
                   "Warehouse", "The Living Waters", "Ossus", "Bescar Shop", "Cafe"]
    skill_sets = {"Fly by using Razorcrest", "Use IB-94 blaster pistol", "Wear beskar armor", "Hint message box"}

    board = {}
    for row in range(5):
        for column in range(5):
            if room_values:
                board[(row, column)] = room_values.pop(random.randint(0, len(room_values) - 1))
            else:
                board[(row, column)] = "Thicket"

    for key in board.keys():
        if key[1] == 4:
            board[key] = "Mandalore Imperial base"

    return board


def make_character():
    print("What be your name Mand'alorian?")
    user_name = input().strip()
    return {"user_name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Skills": [], "Level": 1}


def main():
    """
    Drive the program.
    """

    make_board()
    make_character()


if __name__ == "__main__":
    main()
