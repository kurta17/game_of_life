class Board:
    def __init__(self, width  , height ):
        self.width = width
        self.height = height
        self.board = [ ([False] * width) for i in range(height) ]

    def str_board(self):
        rv = ""
        for m in self.board:
            rv += "".join([".X"[c] for c in m])
            rv += "\n"
        return rv
    
    def place_cell(self,row,col):
        self.board[row][col] = 1

    


