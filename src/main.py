import sys
import time
from os import system

from classes.board import Board
from classes.cell import Cell, CellType
from classes.game import Direction, Game
from classes.snake import Snake
from goaltest import goal_test
from input.user import get_user_input
from movegen import move_gen


def direction_to_string(direction: int):
    if direction == 2:
        return "Up"
    elif direction == -2:
        return "Down"
    elif direction == -1:
        return "Left"
    elif direction == 1:
        return "Right"
    else:
        return "None"


def dfs_search(game: Game):
    stack = [game]
    visited = set()

    while stack:
        current_game = stack.pop()

        system("clear")
        print(current_game.board)
        print(len(stack))

        if goal_test(current_game):
            print("Goal Reached!")
            return True

        visited.add(current_game)

        valid_moves = move_gen(current_game)

        for next_game in valid_moves:
            if next_game not in visited:
                stack.append(next_game)

        time.sleep(0.5)

    return None


def main():
    argc = len(sys.argv)
    sizex = 10
    sizey = 10
    x = 5
    y = 5
    if (argc > 1 and argc < 5) or (argc > 5):
        print(
            "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col>"
        )
        return
    elif argc == 5:
        sizex = int(sys.argv[1])
        sizey = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])

    board = Board(sizex, sizey)
    init_pos = Cell(x, y)
    board.cells[x][y].cell_type = CellType.SNAKE
    init_snake = Snake(init_pos)
    game = Game(init_snake, board, Direction.NONE)
    system("clear")
    game.board.generate_food()

    # Perform DFS search for a solution
    dfs_path = dfs_search(game)

    if dfs_path is False:
        print("No solution found!")
        return

    # for move in dfs_path:
    #     system("clear")
    #     print(game.board)
    #
    #     game.direction = move
    #     game.update()
    #     time.sleep(5)
    #
    #     if game.game_over:
    #         print("Game Over!")
    #         break
    #
    #     if goal_test(game):
    #         print("Goal Reached!")
    #         break


if __name__ == "__main__":
    main()

#
# def main():
#     argc = len(sys.argv)
#     print(argc)
#     sizex = 10
#     sizey = 10
#     x = 5
#     y = 5
#     if (argc > 1 and argc < 5) or (argc > 5):
#         print(
#             "Usage: ./run.sh <board_row_count> <board_col_count> <snake_row> <snake_col>"
#         )
#         print(
#             "OR ./run.sh                                 [uses default values 10 10 5 5]"
#         )
#         return
#     elif argc == 5:
#         sizex = int(sys.argv[1])
#         sizey = int(sys.argv[2])
#         x = int(sys.argv[3])
#         y = int(sys.argv[4])
#
#     board = Board(sizex, sizey)
#     init_pos = Cell(x, y)
#     board.cells[x][y].cell_type = CellType.SNAKE
#     init_snake = Snake(init_pos)
#     game = Game(init_snake, board, Direction.NONE)
#     game.board.generate_food()
#
#     system("clear")
#     print(game.board)
#     board.cells[int(x)][int(y)].cell_type = CellType.EMPTY
#
#     while not game.game_over:
#         system("clear")
#         print(game.board)
#
#         moves = move_gen(game)  # moves are game objects (entire states)
#         goal = goal_test(game)
#
#         if len(moves) == 0:
#             game.game_over = True
#             print("Game Over!")
#             print(f"Goal Reached? {goal}")
#             break
#
#         dirstr = []
#         dirs = []
#         for i in moves:
#             dirs.append(i.direction)
#             if i.direction == 2:
#                 dirstr.append("Up")
#             if i.direction == -2:
#                 dirstr.append("Down")
#             if i.direction == -1:
#                 dirstr.append("Left")
#             if i.direction == 1:
#                 dirstr.append("Right")
#
#         print(f"MoveGen: {dirstr}")
#         print(f"Goal Test: {goal}")
#
#         user_input = get_user_input(dirs)
#
#         if user_input is None:
#             print("Game ended by user")
#             break
#
#         if user_input != Direction.NONE:
#             game.direction = user_input
#
#         game.update()
#
#         # if game.game_over:
#         #     print("Game Over!")
#         #     print(f"Goal Test Reached?: {goal}")
#         #     break
#         # time.sleep(0.5)
#
#
# if __name__ == "__main__":
#     main()
