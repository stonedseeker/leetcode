from typing import List;

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        map = {}
        max = 0
        res = 0
        for i in nums:
            if i in map:
                map[i] += 1
                if map[i] > max:
                    res = i
                    max = map[i]
                
            else: map[i] = 1

        return res


print(Solution().majorityElement([2,2,1,1,1,2,2]))
print(Solution().majorityElement([1,2,1,2]))
