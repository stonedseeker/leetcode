from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def isSafe(row, col, board, n):
            drow = row
            dcol = col

            while row >= 0 and col >= 0:
                if (board[row][col] == 'Q'): return False
                row -= 1
                col -= 1

            col = dcol
            row = drow

            while col >= 0:
                if board[row][col] == 'Q': return False
                col -= 1

            col = dcol

            while row < n and col >= 0:
                if board[row][col] == 'Q': return False
                row += 1
                col -= 1

            return True


        def solve(col, board, res, n):
            if (col == n):
                res.append(res.append(["".join(row) for row in board if board is not None])) 
                return

            for row in range(n):
                if (isSafe(row, col, board, n)):
                    board[row][col] = 'Q'
                    solve(col+1, board, res, n)
                    board[row][col] = '.'
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        print(board)

        res = []
        solve(0, board, res, n)
    
        res = [i for i in res if i is not None]
        return res

print(Solution().solveNQueens(4))
    



