"""
Saeyoung Park
A01344898
"""

import default_settings
import long_prints
import movement
import mini_games
import level_up_stage
import time
import sys


def game():
    """
    Run the game.
    """

    print("Opening the game...")
    time.sleep(3)

    long_prints.mandalore_symbol()

    character = default_settings.make_character()
    long_prints.start_game(character["user_name"])

    board = default_settings.make_board()
    default_settings.show_current_location(board, character)


def main():
    """
    Drive the program.
    """

    if len(sys.argv) != 1:
        print("--------------------------------------------------------------------------------")
        print("Error! Please type correct command: ")
        print("python game.py")
        print("--------------------------------------------------------------------------------")

    else:
        try:
            game()

        except AttributeError:
            print("--------------------------------------------------------------------------------")
            print("Error! Please check file name.")
            print("--------------------------------------------------------------------------------")

        except ValueError:
            print("--------------------------------------------------------------------------------")
            print("Error! Please type a valid command.")
            print("--------------------------------------------------------------------------------")

        except KeyboardInterrupt:
            print("")
            print("--------------------------------------------------------------------------------")
            print("Finished the game through Keyboard input. Good bye.")
            print("--------------------------------------------------------------------------------")

        except SyntaxError:
            print("--------------------------------------------------------------------------------")
            print("Error! Please type correct command: ")
            print("python game.py")
            print("--------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
