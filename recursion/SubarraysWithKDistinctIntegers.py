from typing import List
from collections import defaultdict

class Solution:

    def subarraysWithDistinct(self, nums: List[int], k:int)-> int:
        
        res = []
        self.helper(0,nums, [], res, k)
        print(res)
        return len(res)

    def helper(self, index, nums, lst, res, k):
        if index >= len(nums):
            if self.hasDistinctElements(lst, k):
                res.append(lst.copy())
            return

        lst.append(nums[index])
        self.helper(index+1, nums, lst, res, k)
        lst.pop()
        self.helper(index+1, nums, lst, res, k)

        

            

    def hasDistinctElements(self, nums:List[int], k)-> bool:
                
        s = set()
        for i in nums:
            s.add(i)
        if len(s) != k:
            return False
        return True
nums = [1,2,1,2,3]

print(Solution().subarraysWithDistinct(nums, 2))
