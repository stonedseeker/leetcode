import numpy as np
class Solution:
    def columnWithMaxZeros(self,arr,N):
        # Transpose the matrix
        transposed_arr = [[arr[i][j] for j in range(N)] for i in range(N)]

        print(transposed_arr)
        max_zeros = 0
        max_column = -1  # Initialize max_column to -1
        
        for i in range(N):
            zero_count = transposed_arr[i].count(0)  # Count zeros in the column
            if zero_count > max_zeros:
                max_zeros = zero_count
                max_column = i  # Update max_column
        
        return max_column




nums = [[0, 0, 0],
        [1, 0, 1],
        [0, 1, 1]]
print(np.sum(nums[1] == 0))
print(Solution().columnWithMaxZeros(nums, 3))
