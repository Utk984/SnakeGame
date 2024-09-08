import time
from os import system

from classes.game import Direction, Game


def display_game(game: Game, gtype: str = "", delay: float = 0.5, dir: str = ""):
    system("clear")
    print("SNAKE GAME")
    print(f"mode: {gtype}\n\n")
    print(game.board)
    print(dir)
    time.sleep(delay)


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
