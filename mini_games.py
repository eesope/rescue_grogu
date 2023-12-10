"""
Collection of mini games for each movement, level up, and final stage.
"""
import random


def merit_beskar_lv1():
    """
    Simple game for level 1; can get item.
    """

    print("You are in the Armorer's Space. If you type correct answer,"
          "you can get a helpful item.")
    print("Here is a question.")
    print("")
    print("How many chambers human heart has? Please type a number only.")

    while True:
        answer = input()
        if answer.isnumeric() and int(answer) == 4:
            print("Correct! You earned a Beskar armor.")
            return True
        if answer.isnumeric() and int(answer) != 4:
            print("Incorrect! But, do not worry, you did not lose any HP.")
            return False
        else:
            print("Please type only a number!")


def hp_roll_die_lv2():
    print("You have encountered Jawa who is stealing your belongings. "
          "Shamelessly, they are asking to do a rolling die game if you want your belongings back.")
    print("Which die do you want to try? Please enter 8 or 12 only a number: ")

    while True:
        sides = input()
        if sides.isnumeric():
            if int(sides) == 8 or int(sides) == 12:
                print(f"You will roll 3 times for this {int(sides)} sided die.")
                die_number = random.randint(1, int(sides))
                guess = int(input(f"Enter a number between 1 and {sides} inclusive: "))
                if die_number == guess:
                    print("Lucky! You got back all your belongings.")
                    return True
                if die_number != guess:
                    print("Maybe today is not a day. You damaged by HP -1.")
                    return False
            else:
                print("Which die do you want to roll? 8 or 12")
        else:
            print("Which die do you want to roll? 8 or 12")


def merit_ahsoka_tano_lv2():
    """
    Wild card; ask her help.
    """

    cipher = "rolling stone never moss"
    reversed_cipher = cipher[::-1]
    print("You have encountered Ahsoka Tano. Ahsoka is decoding the message; somehow you know this language.")
    print("Can you translate it to English sentence? You only have one chance to type: ")
    print("--------------------------------------------------------------------------------")
    print(reversed_cipher)
    print("--------------------------------------------------------------------------------")

    answer = input()

    if answer == cipher:
        print("Congrats! It was the correct sentence. You earned a wild card item. "
              "It will be useful later your journey. Be safe, brave one.")
        return True
    else:
        print("It was not the correct sentence. Too bad. Let us move on our journey.")


def merit_razor_crest_lv2():
    """
    Win, and get item.
    """

    print("You found the perfect part for repairing your razor crest ship.")
    print("Answer this question, Jawa will give you the part.")
    print("")
    print("Do you remember what droid does Din Djarin buy from Peli Motto? I need similar android.")

    droid_model = "R5-D4"

    while True:
        answer = input()
        if answer.isalnum() and answer == droid_model:
            print("Hmm.. You are right! Here is the part you told me.")
            return True
        else:
            print("I don't think so. It was not sound like that. Go away.")
            return False


def hp_bones_lv2():
    """
    Win, and get item.
    """

    print("You encountered a monster who collects bones. This monster can do a dark magic.")
    print("Answer this question so that get out of his dark force.")
    print("")
    print("How many bones are in the human body? Please type a number only.")

    while True:
        answer = input()
        if answer.isnumeric() and int(answer) == 206:
            print("Correct! Let us carry on.")
            return True
        if answer.isnumeric() and int(answer) != 206:
            print("Incorrect! You damaged by HP -3")
            return False
        else:
            print("Please type only a number!")


def hp_constant_e_lv3():

    print("If you want to across this shipyards, answer this question.")
    print("")
    print("What is the approximate value of mathematical constant e also known as Euler's number? "
          "Type a float number only until third decimal place. For example, x.xxx"
          "You only have one chance.")

    while True:
        answer = input()
        if answer.isnumeric() and int(answer) == 2.718:
            print("Correct! Let us carry on.")
            return True
        else:
            print("Incorrect! You damaged by HP -5")
            return False


def main():

    merit_beskar_lv1()
    merit_razor_crest_lv2()
    merit_ahsoka_tano_lv2()
    hp_roll_die_lv2()
    hp_bones_lv2()
    hp_constant_e_lv3()


if __name__ == "__main__":
    main()
