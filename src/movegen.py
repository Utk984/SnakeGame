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
            if not state.check_crash(next_cell):
                new_state = create_new_state(state, next_cell, move)
                valid_moves.append(new_state)

    return valid_moves


def create_new_state(
    current_state: Game, next_cell: Cell, direction: Direction
) -> Game:
    game = copy.deepcopy(current_state)
    game.direction = direction
    game.update()
    return game
    #
    # if game.board.cells[next_cell.row][next_cell.col].cell_type == CellType.FOOD:
    #     print("Food is eaten!")
    #     game.snake.move(next_cell)
    #     print(game.snake.head.row, game.snake.head.col)
    #     game.board.generate_food()
    # else:
    #     print("No food")
    #     tail = game.snake.body.pop()
    #     game.board.cells[tail.row][tail.col].cell_type = CellType.EMPTY
    #     game.snake.move(next_cell)
    #     print(game.snake.head.row, game.snake.head.col)
    #
    # # if new_board.cells[next_cell.row][next_cell.col].cell_type == CellType.FOOD:
    # #     print("Food is eaten!")
    # #     new_snake.move(next_cell)
    # #     new_board.cells[next_cell.row][next_cell.col].cell_type = CellType.SNAKE
    # #     print(new_snake.head.row, new_snake.head.col)
    # #     new_board.generate_food()
    # # else:
    # #     print("No food")
    # #     tail = new_snake.body.pop()
    # #     new_board.cells[tail.row][tail.col].cell_type = CellType.EMPTY
    # #     new_snake.move(next_cell)
    # #     new_board.cells[next_cell.row][next_cell.col].cell_type = CellType.SNAKE
    # #     print(new_snake.head.row, new_snake.head.col)
    # #
    # # return Game(new_snake, new_board, Direction.NONE)
    #
    # return game
