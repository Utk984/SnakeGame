from classes.game import Game


def goal_test(state: Game) -> bool:
    return len(state.snake.body) == ((state.board.ROW_COUNT) * (state.board.COL_COUNT))
