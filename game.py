"""
Saeyoung Park
A01344898
"""

import default_settings
import long_prints
import movement
import mini_games
import level_up_stage


def game():
    """
    Run the game.
    """

    print("Opening the game...")
    board = default_settings.make_board()
    character = default_settings.make_character()
    print("------------------------------")

    long_prints.start_game(character)
    long_prints.mandalore_symbol()


def main():
    """
    Drive the program.
    """

    game()


if __name__ == "__main__":
    main()
