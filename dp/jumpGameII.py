from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        root =  nums[0]
        count = 0

        for i in range(len(nums)):
            if root + i == len(nums): return count
            newList = [i for i in nums[count:root + 1]]

            root = max(newList)
            
            count += 1
        return count 
print(Solution().jump([2,3,1,1,4]))
