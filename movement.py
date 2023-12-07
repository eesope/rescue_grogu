"""
Ask, accepts and validate a desired direction of a character; let it move.
"""


def get_user_choice():
    """
    Ask player which direction they want to go.

    """

    move_to = {"w": "North", "d": "East", "s": "South", "a": "West"}
    print("Please type one of w, a, s, or d which is match with your desired direction.")
    print()

    while True:
        print("Please type one of w, a, s, or d which is match with your desired direction.")
        get_direction = input()

        if get_direction.isalpha():
            return move_to[get_direction.strip().lower()]
        else:
            print("Error! Please type only one letter from w, a, s, d which is match with your desired direction.")


def validate_move(board, character, direction):
    """
    Determine whether the desired direction of player is valid or not.

    """

    compass = {"North": -1, "East": 1, "South": 1, "West": -1}
    mock_location = {"mock_x": character["X-coordinate"], "mock_y": character["Y-coordinate"]}

    if direction == "North" or direction == "South":
        mock_location["mock_y"] += compass[direction]

    else:
        mock_location["mock_x"] += compass[direction]
    mock_coordinate = (mock_location["mock_x"], mock_location["mock_y"])

    if mock_coordinate in board.keys():
        return True
    else:
        return False


def move_character(character, direction):
    """
    Take character dictionary and update X and Y coordinates of the character

    """

    compass = {"North": -1, "East": 1, "South": 1, "West": -1}

    if direction == "North" or direction == "South":
        character["Y-coordinate"] += compass[direction]
    elif direction == "East" or direction == "West":
        character["X-coordinate"] += compass[direction]


def check_event(board, character):
    if board[(character["X-coordinate"], character["Y-coordinate"])] ==





















def main():
    pass


if __name__ == "__main__":
    main()
