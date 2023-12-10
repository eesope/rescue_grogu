"""
When initiate game, makes a map and a character.
"""

import random


# how to print grid map
def make_board():
    # [M] == Merit and [D] == Demerit for character
    room_value = [("[M]Lush Veshok Tree Forests", "Fly by using the Razor Crest"),
                  ("[M]The Armorer's Space", "Wear beskar armor"),
                  ("[D]Shipyards", "HP game"),
                  ("[D]Warehouse", "Use IB-94 blaster pistol"),
                  ("[D]The Living Waters", "HP game"),
                  ("[D]Ossus", "HP game"),
                  ("[M]Cafe", "Wild card"),
                  ("[D]Unknown planet", "HP game")]

    board = {}
    for row in range(5):
        for column in range(5):
            board[(row, column)] = room_value[random.randint(0, len(room_value) - 1)]

    for key in board.keys():
        if key[1] == 4:  # [L] == Level up stage
            board[key] = "[L]Mandalore Imperial base"

    return board


def make_character():
    print("What be your name Mand'alorian?")
    user_name = input().strip()
    return {"user_name": user_name, "X-coordinate": 0, "Y-coordinate": 0, "HP": 5, "Skills": [], "Level": 1}


def show_current_location(board, character):
    """
    Take the board and character's coordinates, return the description of character's current location

    :param board: dictionary that has keys as a set of coordinates and values as a short string description
    :param character: dictionary of X, Y coordinates of character, current HP as keys and each values
    :precondition: take the character's coordinates
    :postcondition: print the description of character's location
    """

    # print map and character location
    print(f"Your current location is {board[(character['X-coordinate'], character['Y-coordinate'])][0][3:]}"
          f"and Level {character['Level']}")


def is_alive(character):
    """
    Check if the HP of character is greater than 0.
    """

    if character["HP"] > 0:
        return True
    else:
        return False


def grogu_rescued(board, character):
    """
    Check whether the character has made it to their destination.
    """

    if (character["X-coordinate"], character["Y-coordinate"]) == max(board.keys()):
        return True
    else:
        return False


def main():
    """
    Drive the program.
    """

    board = make_board()
    character = make_character()
    show_current_location(board, character)
    is_alive(character)
    grogu_rescued(board, character)


if __name__ == "__main__":
    main()
