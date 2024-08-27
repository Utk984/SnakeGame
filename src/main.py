from classes.cell import Cell
from classes.snake import Snake
from classes.board import Board
from classes.game import Game, Direction

def main():
    print("Going to start game")
    init_pos = Cell(0, 0)
    init_snake = Snake(init_pos)
    board = Board(10, 10)
    game = Game(init_snake, board)
    game.direction = Direction.RIGHT

    for i in range(5):
        if i == 2:
            game.board.generate_food()
        game.update()
        if i == 3:
            game.direction = Direction.RIGHT
        if game.game_over:
            break

if __name__ == "__main__":
    main()
