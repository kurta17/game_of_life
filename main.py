from board import Board
import time
import random

board = Board(3,3)

def randomize_board(board, density=0.3):
    for row in range(board.height):
        for col in range(board.width):
            if random.random() < density:
                board.place_cell(row, col)

randomize_board(board)
generation = 5


for gen in range(generation):
    print(f'Generation : {gen + 1}')
    print(board.str_board())
    time.sleep(0.5)
    board.next()