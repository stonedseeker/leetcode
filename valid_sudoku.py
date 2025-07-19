from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == ".":
                    continue
                if (grid[r][c] in rows[r] or
                    grid[r][c] in cols[c] or
                    grid[r][c] in squares[(r//3, c//3)]
                ): return False
                rows[r].add(grid[r][c])
                cols[c].add(grid[r][c])
                squares[(r//3, c//3)].add(grid[r][c])
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                if board[r][c] in rows[r]: 
                    return False
                else: 
                    rows[r].add(board[r][c])

                if board[r][c] in cols[c]: 
                    return False
                else: 
                    cols[c].add(board[r][c])

                if board[r][c] in grid[(r//3,c//3)]: 
                    return False
                else: 
                    grid[(r//3,c//3)].add(board[r][c])
        
        return True

      #     0   1   2   3   4   5   6   7   8
board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]


print(Solution().isValidSudoku(board))
