# This file takes user input to play the game

from typing import List

from readchar import readkey, key

from classes.game import Direction


def get_user_input(dirs: List):
    
    while True:
        k = readkey()
        if k == "a" or k == key.LEFT:
            dir = Direction.LEFT
        elif k == "d" or k == key.RIGHT:
            dir = Direction.RIGHT
        elif k == "w" or k == key.UP:
            dir = Direction.UP
        elif k == "s" or k == key.DOWN:
            dir = Direction.DOWN
        elif k == "q":
            dir = None
        else:
            dir = Direction.NONE

        if dir in dirs or dir is None:
            return dir
        else: 
            print("Invalid Input, Try Again")

