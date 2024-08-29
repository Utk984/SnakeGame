import time

from classes.board import Board
from classes.cell import Cell
from classes.game import Direction, Game
from classes.snake import Snake
from input.user import get_user_input


def main():
    print("Going to start game")
    init_pos = Cell(0, 0)
    init_snake = Snake(init_pos)
    board = Board(10, 10)
    game = Game(init_snake, board)
    game.board.generate_food()

    print(
        "Use 'w' (up), 's' (down), 'a' (left), 'd' (right) to move. Press 'q' to quit."
    )

    while not game.game_over:
        # print(game.board)
        user_input = get_user_input()

        if user_input is None:
            print("Game ended by user")
            break

        if user_input != Direction.NONE:
            game.direction = user_input

        game.update()

        if game.game_over:
            print("Game Over!")
            break

        time.sleep(0.5)


if __name__ == "__main__":
    main()
