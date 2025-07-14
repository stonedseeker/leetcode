class Solution:
    def minDeletions(self, s, n): 
        t = s[::-1]
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
        return m - dp[m][n]


print(Solution().minDeletions("agbcba",6))
