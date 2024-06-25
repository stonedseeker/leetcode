from typing import List 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]::
        l = max_sum = 0 
        nums = []

        for l, r in zip(range(0, len(nums) - 1 - k), range(k, len(nums) - 1)):
            s = sum(nums[l:r])
            nums.append(s)
        return max(nums)
nums = 
