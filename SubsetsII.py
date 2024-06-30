from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        def dfs(index, nums, lst, res):
            res.append(lst.copy())

            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                else:
                    lst.append(nums[i])
                    dfs(i + 1, nums, lst, res)
                    lst.pop()
                
            



        res = []
        lst = []

        dfs(0, nums, lst, res)

        return res


nums = [1,2,2]
print(Solution().subsetsWithDup(nums))
       
