def lcs(a,b,m,n,dp):
    if m == 0  or n == 0:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]
    
    if a[m-1] == b[n-1]:
        dp[m][n] = 1 + lcs(a, b, m-1, n-1, dp)
        for i, row in enumerate(dp):
            print(i, " ", row, end='\n')
        print()
        return dp[m][n]
    
    dp[m][n] = max(lcs(a, b, m, n-1, dp), lcs(a,b,m-1,n,dp))
    return dp[m][n]



a = "abcd"
b = "xycd"
m = len(a)
n = len(b)
dp = [[-1 for _ in range(n+1)] for _ in range(m + 1)]


print(lcs(a,b,m,n,dp))

