import random
from typing import Tuple

from classes.cell import Cell, CellType


class Board:
    def __init__(self, row_count: int, col_count: int):
        self.ROW_COUNT = row_count
        self.COL_COUNT = col_count

        self.cells = [
            [Cell(row, col) for col in range(col_count+1)] for row in range(row_count+1)
        ]

    def __str__(self) -> str:
        board_str = "Use 'w' (up), 's' (down), 'a' (left), 'd' (right) to move.\nPress any (wasd) to start. Press 'q' to quit.\n\n┌─"
        for _ in range(len(self.cells)-1):
            board_str += "──"
        board_str += "┐\n"
        for row in self.cells[:-1]:
            board_str += "│ "
            for cell in row[:-1]:
                if cell.cell_type == CellType.EMPTY:
                    board_str += ". "
                elif cell.cell_type == CellType.SNAKE:
                    board_str += "🐍"
                elif cell.cell_type == CellType.FOOD:
                    board_str += "🍎"
            board_str += "│\n"
        board_str += "└─"
        for _ in range(len(self.cells)-1):
            board_str += "──"
        board_str += "┘\n"
        return board_str

    def generate_food(self) -> Tuple[int, int]:
        empty_cells = [
            (row, col)
            for row in range(self.ROW_COUNT)
            for col in range(self.COL_COUNT)
            if self.cells[row][col].cell_type == CellType.EMPTY
        ]
        
        if not empty_cells:
            return (-1, -1)  # No empty cells available
        
        row, col = random.choice(empty_cells)
        self.cells[row][col].cell_type = CellType.FOOD
        print(f"Food is generated at: {row}, {col}")
        return row, col
        
        # while True:
        #     row = random.randint(0, self.ROW_COUNT - 1)
        #     col = random.randint(0, self.COL_COUNT - 1)
        #     if self.cells[row][col].cell_type != CellType.SNAKE:
        #         break
        #
        # self.cells[row][col].cell_type = CellType.FOOD
        # # print(f"Food is generated at: {row}, {col}")
        # return row, col
