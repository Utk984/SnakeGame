import time
from os import system

from classes.game import Direction, Game
from goaltest import goal_test
from movegen import move_gen

# def dfs(game: Game):
#     stack = [game]
#     visited = set()
#
#     while stack:
#         current_game = stack.pop()
#
#         system("clear")
#         print(current_game.board)
#         print(len(stack))
#
#         if goal_test(current_game):
#             print("Goal Reached!")
#             return True
#
#         visited.add(current_game)
#
#         valid_moves = move_gen(current_game)
#
#         for next_game in valid_moves:
#             if next_game not in visited:
#                 stack.append(next_game)
#
#         time.sleep(0.5)
#
#     return False


def dfs(game: Game):
    stack = [(game, None)]
    visited = set()
    predecessors = {}

    while stack:
        current_game, direction = stack.pop()

        system("clear")
        print(current_game.board)

        if goal_test(current_game):
            print("Goal Reached!")
            path = reconstruct_path(predecessors, current_game)
            print("Path to goal:")
            dir = ""
            for game, move in path:
                system("clear")
                if move:
                    dir += direction_to_string(move) + " -> "
                print(game.board)
                print(dir)
                time.sleep(1)
            return True

        visited.add(current_game)

        valid_moves = move_gen(current_game)

        for next_game in valid_moves:
            if next_game not in visited:
                stack.append((next_game, next_game.direction))
                predecessors[next_game] = (current_game, next_game.direction)

        time.sleep(0.5)

    return False


def reconstruct_path(predecessors, goal_game):
    path = []
    current_game = goal_game
    while current_game in predecessors:
        predecessor_game, direction = predecessors[current_game]
        path.append((current_game, direction))
        current_game = predecessor_game
    path.reverse()
    return path


def direction_to_string(direction: Direction) -> str:
    if direction == Direction.RIGHT:
        return "R"
    elif direction == Direction.LEFT:
        return "L"
    elif direction == Direction.UP:
        return "U"
    elif direction == Direction.DOWN:
        return "D"
    return "None"
