class Board:
    def __init__(self, width  , height ):
        self.width = width
        self.height = height
        self.board = [ ([True] * width) for i in range(height) ]

    def str_board(self):
        rv = ""
        for row in self.board:
            rv += "".join(["OX"[c] for c in row])
            rv += "\n"
        return rv


