"""
Collection of mini games for each movement, level up, and final stage.
"""
import random


def merit_lv1():
    """
    Simple game for level 1; can get item.
    """




def hp_roll_die_lv2():
    print("You have encountered foe. Win the rolling die game to continue the adventure.")
    print("Which die do you want to try? Enter 8 or 12: ")

    while True:
        sides = input()
        if sides.isnumeric():
            print(f"You will roll 3 times for this {int(sides)} sided die.")

            die_number = random.randint(3, int(sides) * 3)
            guess = int(input(f"Enter a number between 1 and 5 inclusive: "))

        else:
            print("Enter only a number.")


def merit_quiz():
    """
    Win, and get item.
    """



def ahsoka_tano():
    """
    Wild card; ask her help.
    """






def main():

    merit_lv1()
    hp_roll_die_lv2()
    merit_quiz()



if __name__ == "__main__":
    main()
