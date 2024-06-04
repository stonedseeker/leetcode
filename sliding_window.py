from typing import List

class Solution:
    def slide(self, nums: List[int], k) -> list:
        l = 0
        r = k - 1
        add = sum(nums[l:r+1])
        sums = []
        sums.append(add)

        while r < len(nums) - 1:
            add = add - nums[l]
            
            l += 1
            r += 1
            add = add + nums[r]
            sums.append(add)
            

        return sums

nums = [-1, 2, 3, 3, 4, 5, -1]
print(Solution().slide(nums, 4))
