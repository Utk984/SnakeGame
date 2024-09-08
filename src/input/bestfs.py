from datetime import datetime
from heapq import heappop, heappush
from itertools import count

from classes.game import Game
from goaltest import goal_test
from movegen import move_gen
from utils.utils import direction_to_string, display_game, reconstruct_path


def heuristic(game: Game):
    # Example heuristic: you can refine this as needed
    # Proximity to the nearest food minus the current length of the snake
    # food_distance = (
    #     game.get_distance_to_food()
    # )  # Assuming a method to get the closest food
    snake_length = len(game.snake.body)  # Assuming snake body is represented as a list
    # return food_distance - snake_length
    return -snake_length


def bestfs(game: Game, eval=False):
    # Priority queue to store (heuristic, game, direction)
    pq = []
    counter = count()  # Unique counter to break ties
    heappush(pq, (heuristic(game), next(counter), (game, None)))
    visited = set()
    predecessors = {}
    max_open_size = 0
    t1 = datetime.now()

    while pq:
        _, _, (current_game, direction) = heappop(pq)
        max_open_size = max(max_open_size, len(pq))

        if goal_test(current_game):
            t2 = datetime.now()
            path = reconstruct_path(predecessors, current_game)
            dir = "Start"
            for game, move in path:
                if move:
                    dir += " -> " + direction_to_string(move)
                if not eval:
                    display_game(game, 0, dir)
            return {
                "num_moves": len(path),
                "time": t2 - t1,
                "max_open_size": max_open_size,
                "path": path,
                "goaltest": True,
            }

        visited.add(current_game)

        valid_moves = move_gen(current_game)

        for next_game in valid_moves:
            if next_game not in visited:
                heappush(pq, (heuristic(next_game), next(counter), (next_game, next_game.direction)))
                predecessors[next_game] = (current_game, next_game.direction)

    return None