from enum import IntEnum

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
    def __init__(self, snake: Snake, board: Board, direction: Direction):
        self.snake = snake
        self.board = board
        self.direction = direction
        self.game_over = False

    def update(self):
        # print("Going to update the game")
        if not self.game_over and self.direction != Direction.NONE:
            next_cell = self.get_next_cell(self.direction)
            if self.check_crash(next_cell):
                self.direction = Direction.NONE
                self.game_over = True
            else:
                if next_cell.cell_type == CellType.FOOD:
                    # If next cell is food, don't remove the tail
                    self.snake.move(next_cell)
                    self.board.generate_food()
                else:
                    # Remove tail and then move
                    tail = self.snake.body.pop()
                    tail.cell_type = CellType.EMPTY
                    self.board.cells[tail.row][tail.col].cell_type = CellType.EMPTY
                    self.snake.move(next_cell)

    def get_next_cell(self, direction: Direction) -> Cell:
        # print("Going to find next cell")
        current_position = self.snake.head
        row, col = current_position.row, current_position.col

        if direction == Direction.RIGHT:
            col += 1
        elif direction == Direction.LEFT:
            col -= 1
        elif direction == Direction.UP:
            row -= 1
        elif direction == Direction.DOWN:
            row += 1

        return self.board.cells[row][col]

    def check_crash(self, next_cell: Cell) -> bool:
        return (
            next_cell in self.snake.body
            or next_cell.row < 0
            or next_cell.col < 0
            or next_cell.row >= self.board.ROW_COUNT
            or next_cell.col >= self.board.COL_COUNT
        )

    def __eq__(self, other):
        if not isinstance(other, Game):
            print("Not an instance of Game")
            return False

        for row in range(self.board.ROW_COUNT):
            for col in range(self.board.COL_COUNT):
                if (
                    self.board.cells[row][col].cell_type
                    != other.board.cells[row][col].cell_type
                ):
                    print("Cell type is not equal")
                    return False

        return self.direction == other.direction

    def __hash__(self):
        snake_body_hash = hash(tuple((cell.row, cell.col) for cell in self.snake.body))

        board_hash = hash(
            tuple(tuple(cell.cell_type for cell in row) for row in self.board.cells)
        )

        direction_hash = hash(self.direction)

        return hash((snake_body_hash, board_hash, direction_hash))
