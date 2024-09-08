from datetime import datetime
from os import system
from typing import List

from readchar import key, readkey

from classes.game import Direction
from goaltest import goal_test
from movegen import move_gen
from utils.utils import direction_to_string, display_game


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
    t1 = datetime.now()
    num_moves = 0

    while not game.game_over:
        goal = goal_test(game)
        display_game(game=game, gtype="user", delay=0, dir="")

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
        num_moves += 1

    t2 = datetime.now()
    return {
        "num_moves": num_moves,
        "time": t2 - t1,
        "max_open_size": "NA",
        "goaltest": True,
    }
