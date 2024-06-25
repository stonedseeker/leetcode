from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1"):
                    count += 1
                    self.dfs(grid, i, j)
                    

        return count
        
        
    def dfs(self, grid, i, j):
        
        m = len(grid)
        n = len(grid[0])
        
        
        if i < m and i >= 0 and j < n and j >= 0 and grid[i][j] == '1':

           grid[i][j] = '0'
           self.dfs(grid, i + 1, j)
           self.dfs(grid, i - 1, j)
           self.dfs(grid, i, j + 1)
           self.dfs(grid, i, j - 1)
        
        return grid


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().numIslands(grid))
