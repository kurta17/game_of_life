class Board:
    def __init__(self, width = 3 , height = 3):
        # self.width = width
        # self.height = height
        self.board = [ [False]*3, [False]*3, [False]*3 ]

    def str_board(self):
        rv = ""
        for row in self.board:
            rv += "".join([".O"[c] for c in row])
            rv += "\n"
        return rv


