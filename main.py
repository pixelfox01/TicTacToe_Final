from game import Game
from board import Board


def main():
    board = Board()
    game = Game(board)

    game.board.print_board()


if __name__ == "__main__":
    main()
