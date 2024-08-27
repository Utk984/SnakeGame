from enum import IntEnum
from typing import Tuple

from classes.board import Board
from classes.cell import Cell, CellType
from classes.snake import Snake


class Direction(IntEnum):
    NONE = 0
    RIGHT = 1
    LEFT = -1
    UP = 2
    DOWN = -2


class Game:
    def __init__(self, snake: Snake, board: Board):
        self.snake = snake
        self.board = board
        self.direction = Direction.NONE
        self.game_over = False

    def update(self):
        print("Going to update the game")
        if not self.game_over and self.direction != Direction.NONE:
            next_cell = self.get_next_cell(self.snake.head)
            if self.snake.check_crash(next_cell):
                self.direction = Direction.NONE
                self.game_over = True
            else:
                self.snake.move(next_cell)
                if next_cell.cell_type == CellType.FOOD:
                    self.snake.grow()
                    self.board.generate_food()

    def get_next_cell(self, current_position: Cell) -> Cell:
        print("Going to find next cell")
        row, col = current_position.row, current_position.col

        if self.direction == Direction.RIGHT:
            col += 1
        elif self.direction == Direction.LEFT:
            col -= 1
        elif self.direction == Direction.UP:
            row -= 1
        elif self.direction == Direction.DOWN:
            row += 1

        return self.board.cells[row][col]
