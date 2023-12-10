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

    while default_settings.is_alive(character) and not default_settings.grogu_rescued(board, character):
        default_settings.show_current_location(board, character)
        direction = movement.get_user_choice()
        valid_move = movement.validate_move(board, character, direction)

        if valid_move:
            movement.move_character(character, direction)
            print("-----------------------------------------------------")
            default_settings.show_current_location(board, character)
            print("-----------------------------------------------------")

            hp_battle = movement.check_event(board, character)
            current_lv = character["Level"]

            if hp_battle == "beskar":
                beskar = mini_games.merit_beskar_lv1()
                if beskar:
                    character["Skills"].append("Beskar")

            if hp_battle == "roll_die":
                roll_die = mini_games.hp_roll_die_lv2()
                if not roll_die:
                    character["HP"] -= 1

            if hp_battle == "ahsoka":
                ahsoka = mini_games.merit_ahsoka_tano_lv2()
                if ahsoka:
                    character["Skills"].append("Wisdom")

            if hp_battle == "razor_crest":
                razor_crest = mini_games.merit_razor_crest_lv2()
                if razor_crest:
                    character["Skills"].append("The Razor Crest")

            if hp_battle == "bones":
                bones = mini_games.hp_bones_lv2()
                if not bones:
                    character["HP"] -= 3

            if hp_battle == "constant":
                constant = mini_games.hp_constant_e_lv3()
                if not constant:
                    character["HP"] -= 5

            if (character["X-coordinate"], character["Y-coordinate"]) == (4, 4):
                final_dark = level_up_stage.moff_gideon()
                if final_dark:
                    if default_settings.grogu_rescued(board, character):
                        long_prints.grogu()

            if not hp_battle:
                if current_lv == 1:
                    go_lv2 = level_up_stage.go_lv2()
                    default_settings.is_alive(character)
                    if go_lv2:
                        long_prints.level_up_congrats(character["user_name"])
                        character["Level"] = 2

                if current_lv == 2:
                    go_lv3 = level_up_stage.go_lv3()
                    default_settings.is_alive(character)
                    if go_lv3:
                        long_prints.level_up_congrats(character["user_name"])
                        character["Level"] = 3

    print("")
    long_prints.finish_congrats(character["user_name"])


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
