import random


class Game:
    def __init__(self, board, player_name):
        self.board = board
        self.cur_player = 1
        self.player_name = player_name

    def start(self):
        self.board.print_board()
        while not self.board.check_winner():
            if self.board.check_draw():
                print("It's a draw!")
                return
            if self.cur_player == 1:
                self.player_move()
            else:
                self.computer_move()
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

    # TODO: Implement 2-player mode
    # OR
    # TODO: Implement better AI
    def computer_move(self):
        print("Computer's move...")
        move = random.randint(1, 9)
        valid_move = self.board.make_move(move, self.cur_player)
        while not valid_move:
            move = random.randint(1, 9)
            valid_move = self.board.make_move(move, self.cur_player)
