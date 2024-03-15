class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_board(self):
        print(f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}")
        print("-" * 9)
        print(f"{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")
        print("-" * 9)
        print(f"{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")
