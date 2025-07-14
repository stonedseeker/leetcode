
class Solution:
    def cutRod(self, prices):
        length = [i + 1 for i in range(len(prices))]
        n = len(prices)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(n + 1):
                for x in dp: print(x)
                if length[i-1] <= j:
                    dp[i][j] = max(prices[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][n]


print(Solution().cutRod([1, 5, 8, 9, 10, 17, 17, 20]))
