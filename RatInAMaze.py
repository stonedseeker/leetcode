class Solution:
    def findPath(self, grid):
        
        m, n = len(grid), len(grid[0])

        if grid[m-1][n-1] == 0:
            return -1

        
        res = []
        s = ""
        
        def dfs(i, j, res, s, grid):
            
            m, n = len(grid), len(grid[0])
            if i == m - 1 and j == n - 1:
                res.append(s)
                return

            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            dfs(i+1, j, res, s + "D", grid)
            dfs(i, j-1, res, s + "L", grid)
            dfs(i, j+1, res, s + "R", grid)
            dfs(i-1, j, res, s + "U", grid)

            grid[i][j] = 1
            
     
            
            
            
        dfs(0, 0, res, s, grid)
        
        return res


grid = [
    [1, 0, 0, 0,],
    [1, 1, 0, 1,],
    [1, 1, 0, 0,],
    [0, 1, 1, 1,],
]

grid = [
    [1, 0],
    [1, 0]
]

print(Solution().findPath(grid))
