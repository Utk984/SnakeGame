from os import system
from typing import List

from readchar import key, readkey

from classes.game import Direction
from goaltest import goal_test
from movegen import move_gen
from utils.utils import direction_to_string


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


def user(game):
    goal = False
    while not game.game_over:
        goal = goal_test(game)
        system("clear")
        print(game.board)

        moves = move_gen(game)

        if len(moves) == 0:
            game.game_over = True
            break

        dirstr = []
        dirs = []
        for i in moves:
            dirs.append(i.direction)
            dirstr.append(direction_to_string(i.direction))

        print(f"MoveGen: {dirstr}")
        print(f"Goal Test: {goal}")

        user_input = get_user_input(dirs)

        if user_input is None:
            print("Game ended by user")
            break

        if user_input != Direction.NONE:
            game.direction = user_input

        game.update()

    return goal_test(game)
