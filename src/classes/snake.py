from collections import deque

from classes.cell import Cell, CellType


class Snake:
    def __init__(self, init_pos: Cell):
        self.body = deque([init_pos])
        self.head = init_pos
        self.head.cell_type = CellType.SNAKE

    def move(self, next_cell: Cell):
        print(f"Snake is moving to {next_cell.row}, {next_cell.col}")
        tail = self.body.pop()
        tail.cell_type = CellType.EMPTY

        self.head = next_cell
        self.head.cell_type = CellType.SNAKE
        self.body.appendleft(self.head)

    def check_crash(self, next_cell: Cell) -> bool:
        print("Going to check for Crash")
        return any(cell is next_cell for cell in self.body)
