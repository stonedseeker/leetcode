class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)

        # Initialize the dp table with all zeros
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        
        # Base case: There is 1 way to get sum 0 (using an empty subset)
        # for i in range(n+1):
        #     dp[i][0] = 1
        dp[0][0] = 1
        # Fill the dp table
        for curr_num in range(1, n + 1):
            for curr_sum in range(target + 1):
                                # If the current number can be included in the subset for current_sum
                if arr[curr_num - 1] <= curr_sum:
                    dp[curr_num][curr_sum] = dp[curr_num - 1][curr_sum - arr[curr_num - 1]] + dp[curr_num - 1][curr_sum]
                else:
                    dp[curr_num][curr_sum] = dp[curr_num - 1][curr_sum]
            for x in dp:
                    print(x)
            print()


        # Return the number of ways to form the target sum from the entire array
        for i, x in enumerate(dp):
            print(i, x)
        return dp[n][target]


print(Solution().perfectSum([28, 4, 3, 27, 0, 24, 26], 24))

