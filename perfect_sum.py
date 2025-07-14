class Solution:
    def perfectSum(self, nums, target):
        
        n = len(nums)
        
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)] 
        
        for i in range(n+1):
            dp[i][0] = 1
         
        
        for i in range(1, n+1):
            for j in range(target + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                
        print(dp)
        return dp[n][target] % (10**9 + 7)
        #return dp[n][target]

    
    def perfectSum1(self, arr, target):
        # Initialize dp array
        n = len(arr)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        
        # Base case: there's always 1 way to make sum 0 (by selecting no elements)
        for i in range(n+1):
            dp[i][0] = 1
            
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range( target + 1):  # Start from 0 instead of 1
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[n][target] % (10**9 + 7)  # Usually these problems require modulo


print(Solution().perfectSum([28, 4, 3, 27, 0, 24, 26], 24))
