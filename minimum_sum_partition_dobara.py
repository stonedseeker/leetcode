"""
Input: arr[] = [1, 6, 11, 5]
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
Hence, minimum difference is 1.


Given an array arr[]  containing non-negative integers, the task is to divide it into two sets set1 and set2 such that the absolute difference 
between their sums is minimum and find the minimum difference.
"""



# class solution:
# 	def mindifference(self, arr):
#         target = sum(arr)
#         n = len(arr)
#         dp = [[0 for _ in range(target + 1) for _ in range(n + 1)]]
#
#         dp[0][0] = 1 
#
#         for i in range(1, n+1):
#             for j in range(target+1):
#                 dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j] if arr[i-1] <= j else dp[i-1][j]
#         print(dp)
#
#         mn = 100000000
#         print(dp[n])
#         for i in range(target//2, -1, -1):
#             print(target, dp[n][i])
#             mn = min(mn, target - dp[n][i])
#
#         return mn
#print(solution().mindifferenuce([[1, 6, 11, 5]]))

class Solution:
    def mindifference(self, arr):
        target = sum(arr)
        n = len(arr)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]  # Correcting the list comprehension

         
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j] if arr[i-1] <= j else dp[i-1][j]

        # Print the dp table (just for debugging)
        print(dp)

        mn = 100000000
        print(dp[n], target)
        
        # Find the minimum difference
        for i in range(target//2, -1, -1):
            print(mn, dp[n][i])
            if dp[n][i] != 0:
                print(mn, target - i)
                mn = min(mn, target - 2 * i)

        return mn
print(Solution().mindifference([1, 6, 11, 5]))
