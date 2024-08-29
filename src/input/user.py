# This file takes user input to play the game

import readchar

from classes.game import Direction


def get_user_input():
    key = readchar.readkey()
    if key == "a":
        return Direction.LEFT
    elif key == "d":
        return Direction.RIGHT
    elif key == "w":
        return Direction.UP
    elif key == "s":
        return Direction.DOWN
    elif key == "q":
        return None
    else:
        return Direction.NONE
