"""
Add a doc string
"""

import random


def make_board():
    """
    Take two numbers and create the dictionary of rows * column keys and each descriptive string value.

    :postcondition: dictionary that contains (rows, columns) keys as tuple that contains a set of coordinates
    :return: dictionary that has keys as a set of coordinates and values as a short string description
    """

    room_values = ["Mandalore Imperial base", "Lush Veshok Tree Forests", "The Armorer's Space", "Shipyards",
                   "Warehouse", "The Living Waters", "Ossus", "Bescar Shop", "Cafe"]
    room_events = {}
    lv_up_room = ["Level up dungeon"]

    board = {}
    for row in range(5):
        for column in range(5):
            if room_values:
                board[(row, column)] = room_values.pop(random.randint(0, len(room_values) - 1))
            else:
                board[(row, column)] = "Thicket"

    return board


print(make_board())


# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()
