import sys

class Solution:

    def matrixMultuplicationMemoization(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def dfs(i, j, dp):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                temp = dfs(i, k, dp) + dfs(k+1, j, dp) + arr[i-1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], temp)
            return dp[i][j]
        return dfs(1, n-1, dp)
            
            

    def matrixMultuplication(self, arr):

        def mcmRecursive(i, j):
            # Base case: if there is only one matrix
            if i >= j:
                return 0
            
            min_cost = sys.maxsize
            
            # Try all possible partitions
            for k in range(i, j):
                # Cost = left partition cost + right partition cost + cost of multiplying results
                cost = (mcmRecursive(i, k) +  # Left partition
                        mcmRecursive(k + 1, j) +  # Right partition
                        arr[i-1] * arr[k] * arr[j])  # Cost of multiplying current matrices
                
                min_cost = min(min_cost, cost)
            
            return min_cost
        return mcmRecursive(1, n-1)
    
arr = [2, 1, 3, 4]
sol = Solution()
print(sol.matrixMultuplicationMemoization(arr))
