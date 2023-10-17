from board import Board

board = Board(3,3)
# next_boar = board.next_board()
for x in range(board.height):
    board.place_cell(1,x)

print(board.str_board())


print(board.str_board())


print(board.str_board())