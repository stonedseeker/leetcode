class Solution:
    def minDifference(self, arr):
    #first use subset sum to get a matrix of the sums of the subset that can be used to get the answer
    
        n = len(arr)
        rng = sum(arr)
        
        dp = [[False for _ in range(rng + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, rng + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        max_sum = 0
        for j in range(rng // 2, -1, -1):
            print(dp[n][j], j)
        for j in range(rng // 2, -1, -1):  # Iterate from the middle down
            if dp[n][j]:
                max_sum = j
                break
        for x in dp:
            print(x)
        # The minimum difference is twice the difference between the total sum and the maximum subset sums
        print("range = ", rng, "max_sum = ", max_sum)
        return rng - 2 * max_sum


print(Solution().minDifference([7, 8, 6, 4, 2, 9, 10, 3, 8, 2, 4, 4, 9, 9,7, 6, 2, 8, 9, 5, 6, 7, 3, 2, 3, 1, 2, 2, 10,9, 6, 10, 2, 3, 8, 9, 3]))
#print(Solution().minDifference([6, 8, 6, 4, 2, 9, 10, 3, 8, 2, 4, 4, 9, 9, 7, 1, 6, 2, 8, 9, 5, 6, 7, 3, 2, 3, 1, 2, 2, 10, 9, 6, 10, 2, 3, 8, 9, 3]))

