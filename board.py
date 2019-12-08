import numpy as np
from Player import *


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0]*self.cols]*self.rows

    def print_board(self):
        print(np.flip(self.board, 0))

    def get_next_open_row(self, col):
        print(type(col))
        for rows in range(self.rows):
            if self.board[rows][col] == 0:
                return rows
