
'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

from types import MappingProxyType
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        max_len = 0
        num_zeroes = 0

        while r < len(nums):
            if nums[r] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if nums[l] == 0:
                    num_zeroes -= 1
                l += 1
                
            # print(l, r, sep = ' ')
            max_len = max(max_len, r - l + 1)
            print(l, r, max_len, sep = ' ')

            r += 1
        return max_len

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(Solution().longestOnes(nums, k))
