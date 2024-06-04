from typing import List
from collections import defaultdict

class Solution:

    
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int, {0: 1})
        s = 0
        result = 0
        for n in nums:
            s += n
            result += sums[s-k]
            print(f'result = {result} ')
            print(f'sums = {sums} ')
            sums[s] += 1
            
        return result

    def helper(self, index, nums, lst, res, k):
        if (index == len(nums)):
            if (sum(lst) == k):
                res.append(lst[:])
            return 

        lst.append(nums[index])
        self.helper(index + 1, nums, lst, res, k)
        lst.pop()
        self.helper(index + 1, nums, lst, res,k)


    def subarraySum1(self, nums: List[int], k: int) -> int:
        res = []
        self.helper(0, nums, [], res, k)
        for i in res:
            print(i)
        return len(res)
    
nums = [1,1,1]
print(Solution().subarraySum(nums, 2))
