#!/usr/bin/python

board = []

for i in range(5):
    board.append(['O', 'O', 'O', 'O', 'O'])

def print_board(board_in):
    for i in range(len(board)):
        print board[i]

print_board(board)

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

random_col(board)
random_row(board)