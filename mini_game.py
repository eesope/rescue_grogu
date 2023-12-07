"""
Collection of mini games for each movement, level up, and final stage.
"""
import random


def guessing_game(character):
    """
    Check whether the randomly picked number and user picked number is same or not.

    """

    print("You have encountered foe. Win the guessing game to continue the game.")
    secret_number = random.randint(1, 5)
    guess = int(input(f"Enter a number between 1 and 5 inclusive: "))
    if guess == secret_number:
        print("Correct!")
    else:
        character["Current HP"] -= 1
        print("Wrong number. Your have lost HP by 1.")
        print(f"Your current HP: {character['Current HP']}.")


def roll_die():
    """
    Roll a die with the specified number of sides the specified number of times.

    :param rolls: an int
    :param sides: an int
    :precondition: rolls must be an int
    :precondition: sides must be an int
    :postcondition: rolls the die of the specified size the specified number of times
    :return: random sum of rolls
    """
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


    return True


def main():
    pass


if __name__ == "__main__":
    main()
