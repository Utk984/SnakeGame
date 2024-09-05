import copy
from typing import List

from classes.game import Direction, Game


def move_gen(game: Game) -> List[Game]:
    possible_moves = [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]
    valid_moves = []

    state = copy.deepcopy(game)

    for move in possible_moves:
        if move != -state.direction:
            next_cell = state.get_next_cell(move)
            if not state.check_crash(next_cell):
                new_state = create_new_state(state, move)
                valid_moves.append(new_state)

    return valid_moves


def create_new_state(current_state: Game, direction: Direction) -> Game:
    game = copy.deepcopy(current_state)
    game.direction = direction
    game.update()
    return game
