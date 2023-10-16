from board import Board

board = Board(3,3)
for x in range(board.height):
    board.place_cell(1,x)

print(board.str_board())
board.next()
print(board.str_board())