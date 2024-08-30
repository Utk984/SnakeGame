from os import system

from classes.board import Board
from classes.cell import Cell, CellType
from classes.game import Direction, Game
from classes.snake import Snake
from goaltest import goal_test
from input.user import get_user_input
from movegen import move_gen


def main():
    size = int(input("Enter grid size: "))
    x = int(input("Enter initial snake row: "))
    y = int(input("Enter initial snake column: "))

    board = Board(size, size)
    init_pos = Cell(x, y)
    board.cells[x][y].cell_type = CellType.SNAKE
    init_snake = Snake(init_pos)
    game = Game(init_snake, board, Direction.NONE)
    game.board.generate_food()

    system("clear")
    print(game.board)
    board.cells[int(x)][int(y)].cell_type = CellType.EMPTY

    while not game.game_over:
        system("clear")
        print(game.board)

        moves = move_gen(game)
        if len(moves) == 0:
            game.game_over = True
            print("Game Over!")
            break

        dirstr = []
        dirs = []
        for i in moves:
            dirs.append(i.direction)
            if i.direction == 2:
                dirstr.append("Up")
            if i.direction == -2:
                dirstr.append("Down")
            if i.direction == -1:
                dirstr.append("Left")
            if i.direction == 1:
                dirstr.append("Right")

        print(f"MoveGen: {dirstr}")
        print(f"Goal Test: {goal_test(game)}")

        user_input = get_user_input(dirs)

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
