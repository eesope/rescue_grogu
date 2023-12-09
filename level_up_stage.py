"""
Collection of mini games for each movement, level up, and final stage.
"""
import random


def go_lv2():
    """
    Win this game, you are now level 2 player.
    """

    # "question": "The binary number 10111100110; is equivalent to the Decimal number 1510"
    # "correct_answer": "True"


def go_lv3():
    """
    Win this game, you are now level 3 player.
    """

    # "question": "The hexadecimal number 7E7; is equivalent to the Decimal number"
    # "correct_answer": "2023"


def moff_gideon():
    """
    Defeat him through a palindrome, you will resque Grogu.
    """

    print("Give one palindrome; it must include more than 4 alphabets: ")
    answer = input()
    until = len(answer) // 2

    if until >= 2:
        chance = 0
        for count in range(until):
            if answer[count] == answer[-(count + 1)]:
                print(f"Passed examine letter #{count + 1}. {3 - count} test(s) left...")

            if answer[count] != answer[-(count + 1)]:
                chance += 1
                print(f"You have 3 chances; {3 - chance} left.")
                if chance == 3:
                    print("You lose all your chance. I will take Grogu and his force.")
                    return False
                else:
                    print("Give one palindrome; it must include more than 4 alphabets: ")
                    answer = input()



def main():

    go_lv2()
    go_lv3()
    moff_gideon()


if __name__ == "__main__":
    main()
