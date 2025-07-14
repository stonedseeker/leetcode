class Solution:
    def print_lcss(self,s,t):
        m = len(s)
        n = len(t)
        res = ""
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp)

        i, j = m,n 
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:  # Characters match, part of LCS
                res += s[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
                i -= 1
            else:  
                j -= 1
        return res




print(Solution().print_lcss("abcdaf", "acbcd"))
