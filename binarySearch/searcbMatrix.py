from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COLUMN = len(matrix), len(matrix[0])

        top, bot = 0, ROW - 1

        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][-1]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        if not (top <= bot): 
            return False
        
        row = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False 

matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
print(Solution().searchMatrix(matrix, 3))

        
