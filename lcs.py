class Solution_prev:
    def lcs(self,s,t):
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
        return dp[m][n]





class Solution:
    def lcs(self, s, t):
        m = len(s)
        n = len(t)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]


print(Solution().lcs("abcd", "abced"))



''''
in problems that require us to use the max or min operator then each rows first characted also has to be characted
'''
