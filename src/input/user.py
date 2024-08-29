# This file takes user input to play the game

from typing import List

import readchar

from classes.game import Direction


def get_user_input(dirs: List):
    
    while True:
        key = readchar.readkey()
        if key == "a":
            dir = Direction.LEFT
        elif key == "d":
            dir = Direction.RIGHT
        elif key == "w":
            dir = Direction.UP
        elif key == "s":
            dir = Direction.DOWN
        elif key == "q":
            dir = None
        else:
            dir = Direction.NONE

        if dir in dirs:
            return dir
        else: 
            print("Invalid Input, Try Again")

