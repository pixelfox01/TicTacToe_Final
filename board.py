class Board:
    def __init__(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-" * 11)
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-" * 11)
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    def make_move(self, move, player):
        move = int(move) - 1
        if self.board[move] == "X" or self.board[move] == "O":
            return False
        else:
            self.board[move] = "X" if player == 1 else "O"
            return True
