class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        
        def lcs(str1, str2, m, n, dp):
            if m == 0 or n == 0:
                return 0

            if dp[m][n] != -1:
                return dp[m][n]

            if str1[m-1] == str2[n-1]:
                dp[m][n] = 1 + lcs(str1, str2, m-1, n-1, dp)
            else:
                dp[m][n] = max(lcs(str1, str2, m-1, n,dp), lcs(str1, str2, m, n-1,dp))

            return dp[m][n]

        result = []
        i, j = m, n

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
                result.append(str1[i])
            else:
                j -= 1
                result.append(str2[j])

        while i > 0:
            result.append(str1[i-1])
            i -= 1

        while j > 0:
            result.append(str2[j-1])
            j -= 1

        return "".join(result)


a = "abcd"
b = "xycd"

print(Solution().shortestCommonSupersequence(a,b))

        
