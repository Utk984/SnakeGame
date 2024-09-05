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
        player = 1
    elif argc == 6:  # set own args
        sizex = int(sys.argv[1])
        sizey = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        player = int(sys.argv[5])
    else:  # incorrect args
        print(
            "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col> <player>"
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
    goal = dfs(game) if player == 1 else bfs(game) if player == 2 else user(game)
    print("Game Over!")

    if goal:
        if player == 1 or player == 2:
            print("Time: ", goal["time"])
            print("Number of Moves: ", goal["num_moves"])
            print("Max Open Size: ", goal["max_open_size"])
        print("Goal Test Reached!!!")
    else:
        print("Goal Test Not Reached!!!")


if __name__ == "__main__":
    main()
