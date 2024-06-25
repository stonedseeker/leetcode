from typing import List


class Solution:
     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        def dfs(index, nums, lst, res):
            
            if index == len(nums):
                if sum(lst) == target:
                    res.append(lst.copy())
                return 
            
            lst.append(nums[index])
            dfs(index + 1, nums, lst, res)
            lst.pop(len(lst) - 1)
            dfs(index + 1, nums, lst, res)

        res = []
        lst = []
        
        dfs(0, nums, lst, res)

        sizes = [len(i) for i in res]
        
        print(res)
        print(sizes)
        return min(sizes) if sizes else 0
            
        


nums = [2,3,1,2,4,3]
target = 213
nums = [1,1,1,1,1,1,1,1]
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
print(Solution().minSubArrayLen(target, nums))

