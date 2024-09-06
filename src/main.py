import sys
from os import system

from classes.board import Board
from classes.cell import Cell, CellType
from classes.game import Direction, Game
from classes.snake import Snake
from input.bfs import bfs
from input.dfs import dfs
from input.user import user


def main():
    argc = len(sys.argv)
    if argc == 1:  # default args
        sizex = 4
        sizey = 4
        x = 1
        y = 1
        player = "user"
    elif argc == 6:  # set own args
        sizex = int(sys.argv[1])
        sizey = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        player = sys.argv[5]
        if player not in ("user", "bfs", "dfs", "bestfs"):
            print(
                "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col> <user/bfs/dfs/bestfs>"
            )
            return
    else:  # incorrect args
        print(
            "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col> <user/bfs/dfs/bestfs>"
        )
        return

    # setup
    board = Board(sizex, sizey)
    init_pos = Cell(x, y)
    board.cells[x][y].cell_type = CellType.SNAKE
    init_snake = Snake(init_pos)
    game = Game(init_snake, board, Direction.NONE)
    system("clear")
    game.board.generate_food()

    # game
    goal = dfs(game) if player == "dfs" else bfs(game) if player == "bfs" else user(game)
    print("Game Over!")

    if goal:
        if player == "bfs" or player == "dfs":
            print("Time: ", goal["time"])
            print("Number of Moves: ", goal["num_moves"])
            print("Max Open Size: ", goal["max_open_size"])
        print("Goal Test Reached!!!")
    else:
        print("Goal Test Not Reached!!!")


if __name__ == "__main__":
    main()
