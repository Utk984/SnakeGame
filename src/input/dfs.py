from datetime import datetime

from classes.game import Game
from goaltest import goal_test
from movegen import move_gen
from utils.utils import direction_to_string, display_game, reconstruct_path


def dfs(game: Game, eval=False):
    stack = [(game, None)]
    visited = set()
    predecessors = {}
    max_open_size = 0
    t1 = datetime.now()

    while stack:
        current_game, direction = stack.pop()
        max_open_size = max(max_open_size, len(stack))

        # system("clear")
        # print(current_game.board)
        # time.sleep(0.1)

        if goal_test(current_game):
            t2 = datetime.now()
            path = reconstruct_path(predecessors, current_game)
            dir = "Start"
            for game, move in path:
                if move:
                    dir += " -> " + direction_to_string(move)
                if not eval:
                    display_game(game, 0.5, dir)
            return {
                "num_moves": len(path),
                "time": t2 - t1,
                "max_open_size": max_open_size,
                "path": path,
            }

        visited.add(current_game)

        valid_moves = move_gen(current_game)

        for next_game in valid_moves:
            if next_game not in visited:
                stack.append((next_game, next_game.direction))
                predecessors[next_game] = (current_game, next_game.direction)

    return None
