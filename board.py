class Board:
    def __init__(self):
        # TODO: Implement board with 2D list
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

    def check_winner(self):
        for i in range(0, 3):
            # Check columns
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True
            # Check rows
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2]:
                return True

        # Check main diagonal
        if self.board[0] == self.board[4] == self.board[8]:
            return True

        # Check other diagonal
        if self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def check_draw(self):
        for cell in self.board:
            if cell != "X" and cell != "O":
                return False
        return True
