from typing import List

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

            res = []

            def dfs(start, res):
                if start == len(nums):
                    res.append(nums.copy())
                    return
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    dfs(start + 1, res)
                    nums[start], nums[i] = nums[i], nums[start]
            dfs(0, res)
            return res
                
                



    def permute_with_space(self, nums: List[int]) -> List[List[int]]:
        
        map = {}
        for i in nums:
            map[i] = 0
    
        print(nums)

        def dfs(nums, map, lst, res):
            
            if len(lst) == len(nums):
                res.append(lst.copy())

            for i in range(len(nums)):
                if map[nums[i]] != 1:
                    lst.append(nums[i])
                    map[nums[i]] = 1
                    dfs(nums, map, lst, res)
                    map[nums[i]] = 0
                    lst.pop()
                    

        res = []
        dfs(nums, map, [], res)
        return res

nums = [1,2,3]
print(Solution().permute(nums))
