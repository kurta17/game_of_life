class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [([False] * width) for i in range(height)]
        self.next_board = [([False] * self.width) for i in range(self.height)]
        
        

    def str_board(self):
        rv = ""
        for m in self.board:
            rv += "".join([".X"[c] for c in m])
            rv += "\n"
        return rv

    def place_cell(self, row, col):
        self.board[row][col] = 1

    def next(self):
        for row_num in range(self.width):
            for col_num in range(self.height):
                n = self.count_live_neigh(row_num, col_num)
                if self.board[row_num][col_num]:
                    if n < 2 or n > 3:
                        self.next_board[row_num][col_num] = False
                    else:
                        self.next_board[row_num][col_num] = True
                else:
                    if n == 3:
                        self.next_board[row_num][col_num] = True
        self.board, self.next_board = self.next_board, self.board
        
        
         

    def count_live_neigh(self,row,col):
        count = 0
        for r in (-1,0,1):
            for c in (-1,0,1):
                if r == c and r == 0:
                    continue 
                if self.get_cell(row+r,col+c):
                    count += 1
        return count
    
    def get_cell(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.board[row][col]
        return False




