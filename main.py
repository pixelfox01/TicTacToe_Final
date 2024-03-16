from game import Game
from board import Board


def main():
    board = Board()
    print("Welcome to Tic Tac Toe!")
    player_name = input("Enter your name: ")
    game = Game(board, player_name)
    game.start()

    print("Game over!")


if __name__ == "__main__":
    main()
