from collections import deque

from classes.cell import Cell, CellType


class Snake:
    def __init__(self, init_pos: Cell):
        self.body = deque([init_pos])
        self.head = init_pos
        self.head.cell_type = CellType.SNAKE

    def move(self, next_cell: Cell):
        self.body.appendleft(next_cell)
        self.head = next_cell
        self.head.cell_type = CellType.SNAKE
