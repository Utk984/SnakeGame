import sys
from os import system

from classes.board import Board
from classes.cell import Cell, CellType
from classes.game import Direction, Game
from classes.snake import Snake
from input.ai import dfs
from input.user import user


def main():
    argc = len(sys.argv)
    sizex = 10
    sizey = 10
    x = 5
    y = 5
    if (argc > 1 and argc < 6) or (argc > 6):
        print(
            "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col> <player>"
        )
        return
    elif argc == 6:
        sizex = int(sys.argv[1])
        sizey = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        player = int(sys.argv[5])

    board = Board(sizex, sizey)
    init_pos = Cell(x, y)
    board.cells[x][y].cell_type = CellType.SNAKE
    init_snake = Snake(init_pos)
    game = Game(init_snake, board, Direction.NONE)
    system("clear")
    game.board.generate_food()

    if player == 1:
        goal = dfs(game)
    elif player == 0:
        goal = user(game)

    print("Game Over!")
    print(f"Goal Test Reached? {goal}")


if __name__ == "__main__":
    main()
