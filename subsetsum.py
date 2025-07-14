class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True 

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                
                if arr[i-1] <= j:
                    dp[i][j] = dp[i][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        for i in dp:
            print(i)

        return dp[n][target]

            


print(Solution().isSubsetSum([1,2,3],6))
