from board import *
import random as rand
turn = rand.randint(0, 1)


class players:
    def __init__(self, piece):
        self.piece = piece


    def make_move(self, board):
        col = input("Make a move 0-6: ")
        col = (int) (col)
        row = board.get_next_open_row(col)
        self.drop_piece(board, row, col)

    def drop_piece(self, board, row, col):
        board[row][col] = self.piece

