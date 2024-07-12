from typing import List

class Solution:
     def countSmaller(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)

        for i in range(len(nums) - 1):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            res[i] = count
        
        return res



nums = [5,2,6,1]
print(Solution().countSmaller(nums))
