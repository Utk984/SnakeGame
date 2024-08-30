import copy
from typing import List

from classes.cell import Cell, CellType
from classes.game import Direction, Game


def move_gen(game: Game) -> List[Game]:
    possible_moves = [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]
    valid_moves = []

    state = copy.deepcopy(game)

    for move in possible_moves:
        if move != -state.direction:  # Prevent 180-degree turns
            next_cell = state.get_next_cell(move)
            print(next_cell.row, next_cell.col)
            if not state.check_crash(next_cell):
                new_state = create_new_state(state, next_cell, move)
                valid_moves.append(new_state)

    return valid_moves


def create_new_state(
    current_state: Game, next_cell: Cell, direction: Direction
) -> Game:
    new_board = copy.deepcopy(current_state.board)
    new_snake = copy.deepcopy(current_state.snake)

    if next_cell.cell_type == CellType.FOOD:
        # If next cell is food, don't remove the tail
        new_snake.move(next_cell)
        new_board.generate_food()
    else:
        # Remove tail and then move
        tail = new_snake.body.pop()
        tail.cell_type = CellType.EMPTY
        new_snake.move(next_cell)

    return Game(new_snake, new_board, direction)
