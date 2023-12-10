"""
When initiate game, makes a map and a character.
"""

import random


# how to print grid map
def make_board():
    # [#] == character level
    lv1_rooms = [("[1]The Armorer's Space", "beskar"), ("Thicket")]
    lv3_rooms = [("[3]Shipyards", "constant"), ("Thicket")]
    lv2_rooms = [("[2]Lush Veshok Tree Forests", "razor_crest"),
                  ("[2]Warehouse", "roll_die"),
                  ("[2]The Living Waters", "ahsoka"),
                  ("[2]Ossus", "razor_crest"),
                  ("[2]Cafe", "roll_die"),
                  ("[2]Unknown planet", "bones")]

    board = {}
    for row in range(5):
        for column in range(5):
            if row == 0:
                board[(row, column)] = lv1_rooms[random.randint(0, len(lv1_rooms) - 1)]
            if row == 1 or row == 2 or row == 3:
                board[(row, column)] = lv2_rooms[random.randint(0, len(lv2_rooms) - 1)]
            if row == 4:
                board[(row, column)] = lv3_rooms[random.randint(0, len(lv3_rooms) - 1)]

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
