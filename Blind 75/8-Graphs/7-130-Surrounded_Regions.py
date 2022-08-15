
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # O(n * m)
        
        ROWS, COLUMNS = len(board), len(board[0])
        
        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLUMNS or board[r][c] != "O":
                return 
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # (1): Capture unsurrounded regions (O -> T) --> DFS
        for r in range(ROWS):
            for c in range(COLUMNS):
                
                # Only focus on the border of the board
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLUMNS - 1])):
                    capture(r, c)
        
        # (2): Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        # (3): Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                    
        