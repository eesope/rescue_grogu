"""
Collection of mini games for each movement, level up, and final stage.
"""


def go_lv2():
    """
    Win this game, you are now level 2 player.
    """

    print("Hello, the guardian of the child.")
    print("Answer this question to be a level 2; get a higher HP.")
    print("")
    print("The binary number 10111100110; is equivalent to the Decimal number 1510. True or False?")
    print("You only have one chance.")

    answer = input()
    if answer.lower() == "true":
        print("Correct. Wish you safe trip.")
        return True
    else:
        print("You may need to train more, brave one.")
        return False


def go_lv3():
    """
    Win this game, you are now level 3 player.
    """

    print("Hello, the guardian of the child.")
    print("Answer this question to be a level 3, finally.")
    print("")
    print("The hexadecimal number 7E7; is equivalent to the Decimal number 2023. True or False?")
    print("You only have one chance.")

    answer = input()
    if answer.lower() == "true":
        print("Correct. Your child is around here. Wish you the best of luck.")
        return True
    else:
        print("You may need to train more, brave one.")
        return False


def moff_gideon():
    """
    Defeat him through a palindrome, you will resque Grogu.
    """

    print("You eventually came here, the guardian of the child.")
    print("Answer this question. If failed, the force is mine.")
    print("")

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
        print("Finally! You defeated Moff Gideon; rescued Grogu!")
        return True


def main():

    # go_lv2()
    # go_lv3()
    moff_gideon()


if __name__ == "__main__":
    main()
