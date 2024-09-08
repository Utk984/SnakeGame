import random

from tqdm import tqdm

from classes.board import Board
from classes.cell import Cell, CellType
from classes.game import Direction, Game
from classes.snake import Snake
from input.bestfs import bestfs
from input.bfs import bfs
from input.dfs import dfs
from utils.plots import plots


def run_comparisons(board_size, bfs_eval=True):
    results = []
    for i in tqdm(board_size):
        game = create_random_game(i)

        dfs_result = dfs(game, eval=True)
        if bfs_eval:
            bfs_result = bfs(game, eval=True)
        else:
            bfs_result = None
        best_result = bestfs(game, eval=True)

        results.append((dfs_result, bfs_result, best_result))
    return results


def create_random_game(board_size: int) -> Game:
    snake_x = random.randint(0, board_size - 1)
    snake_y = random.randint(0, board_size - 1)

    board = Board(board_size, board_size)
    snake_pos = Cell(snake_x, snake_y)
    board.cells[snake_x][snake_y].cell_type = CellType.SNAKE
    snake = Snake(snake_pos)
    game = Game(snake, board, Direction.NONE)

    board.generate_food()

    return game


if __name__ == "__main__":
    results = run_comparisons([3] * 10)
    plots(results)

    results = run_comparisons([2, 3, 4, 5, 6, 7, 8], bfs_eval=False)
    plots(results)
