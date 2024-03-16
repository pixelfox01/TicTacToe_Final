import random


class Game:
    def __init__(self, board, player_name):
        self.board = board
        self.cur_player = 1
        self.player_name = player_name

    def start(self):
        self.board.print_board()
        while not self.check_winner():
            if self.check_draw():
                print("It's a draw!")
                return
            if self.cur_player == 1:
                self.player_move()
            else:
                self.player_move()
            self.board.print_board()
            self.switch_player()
        print(f"{self.player_name} wins!" if self.cur_player == 2 else "Computer wins!")

    def switch_player(self):
        self.cur_player = 1 if self.cur_player == 2 else 2

    def player_move(self):
        move = int(input(f"{self.player_name}, enter cell number to make your move: "))
        valid_move = self.board.make_move(move, self.cur_player)
        while not valid_move:
            print("Invalid move!")
            move = input(f"{self.player_name}, enter cell number to make your move: ")
            valid_move = self.board.make_move(move, self.cur_player)

    def get_computer_move(self):
        print("Computer's move...")
        move = random.randint(1, 9)
        valid_move = self.board.make_move(move, self.cur_player)
        while not valid_move:
            move = random.randint(1, 9)
            valid_move = self.board.make_move(move, self.cur_player)

    def check_winner(self):
        for i in range(0, 3):
            if (
                self.board.board[i]
                == self.board.board[i + 3]
                == self.board.board[i + 6]
            ):
                return True
            if (
                self.board.board[i * 3]
                == self.board.board[i * 3 + 1]
                == self.board.board[i * 3 + 2]
            ):
                return True
        if self.board.board[0] == self.board.board[4] == self.board.board[8]:
            return True
        if self.board.board[2] == self.board.board[4] == self.board.board[6]:
            return True
        return False

    def check_draw(self):
        for cell in self.board.board:
            if cell != "X" and cell != "O":
                return False
        return True
