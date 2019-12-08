from board import *
import Player
import random as rand

def main():
    b1 = Board(6, 7)
    p1 = Player.players(1)
    p2 = Player.players(2)
    turn = rand.randint(0, 1)
    Board.print_board(b1)
    game_over = False
    while not game_over:
        if turn == 0:
            p1.make_move(b1)
        else:
            p2.make_move(b1)
        turn = update_turn(turn)

def update_turn(turn):
    if turn == 1:
        nturn = turn % 2
    else:
        nturn = turn + 1
    return nturn


if __name__ == "__main__":
    main()

