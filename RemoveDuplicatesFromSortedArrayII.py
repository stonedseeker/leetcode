from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        res = []

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        for i in range(len(nums)):
            if map[nums[i]] >= 2:
                res.append(nums[i])
                res.append(nums[i])
                map[nums[i]] = -1
            else:
                res.append(nums[i])
        print(res)
        return len(res)

nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))
