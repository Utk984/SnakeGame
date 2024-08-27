import random
from typing import List, Tuple

from classes.cell import Cell, CellType


class Board:
    def __init__(self, row_count: int, col_count: int):
        self.ROW_COUNT = row_count
        self.COL_COUNT = col_count

        self.cells = [
            [Cell(row, col) for col in range(col_count)] for row in range(row_count)
        ]

    def generate_food(self) -> Tuple[int, int]:
        print("Going to generate food")
        while True:
            row = random.randint(0, self.ROW_COUNT - 1)
            col = random.randint(0, self.COL_COUNT - 1)
            if self.cells[row][col].cell_type != CellType.SNAKE:
                break

        self.cells[row][col].cell_type = CellType.FOOD
        print(f"Food is generated at: {row}, {col}")
        return row, col
