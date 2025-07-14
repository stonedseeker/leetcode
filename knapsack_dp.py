class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSacsk(self, capacity, val, wt):
        
        
        n = min(len(val), len(wt))

        dp = [[0 for _ in range(capacity+1)] for _ in range(n + 1)]

        print(dp)
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0

                if wt[i-1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
                else: dp[i][j] = dp[i-1][j]
        

        return dp[n][capacity]
        
    def knapSack(self, capacity, val, wt):
        n = len(val)  # Assuming val and wt have the same length

        dp = [[0 for _ in range(n+1)] for _ in range(capacity+1)]

        print(dp)
        for i in range(1, capacity + 1):
            for j in range(1, n+1):
                if wt[j] <= i:
                    dp[i][j] = max(val[j] + dp[i - wt[j]][j - 1], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i][j - 1]
        print(dp)
        return dp[capacity][n - 1]

print(Solution().knapSack(5, [10, 40, 30, 50], [5, 4, 6, 3]))
