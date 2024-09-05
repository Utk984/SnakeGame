import time
from os import system

from classes.game import Game
from goaltest import goal_test
from movegen import move_gen


def dfs(game: Game):
    stack = [game]
    visited = set()

    while stack:
        current_game = stack.pop()

        system("clear")
        print(current_game.board)
        print(len(stack))

        if goal_test(current_game):
            print("Goal Reached!")
            return True

        visited.add(current_game)

        valid_moves = move_gen(current_game)

        for next_game in valid_moves:
            if next_game not in visited:
                stack.append(next_game)

        time.sleep(0.5)

    return False
