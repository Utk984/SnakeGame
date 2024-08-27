# To represent a cell of display board

from enum import Enum

class CellType(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2

class Cell:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.cell_type: CellType = CellType.EMPTY

