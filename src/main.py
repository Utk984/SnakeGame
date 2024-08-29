from os import system

from classes.board import Board
from classes.cell import Cell
from classes.game import Direction, Game
from classes.snake import Snake
from input.user import get_user_input


def main():
    init_pos = Cell(5, 5)
    board = Board(10, 10)
    init_snake = Snake(init_pos)
    game = Game(init_snake, board)
    system("clear")
    game.board.generate_food()

    print(game.board)

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

        # time.sleep(0.5)


if __name__ == "__main__":
    main()
