from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        lst = []

        nums.sort()
        print(nums)

        def dfs(index, nums, lst, res):
            if index == len(nums):
                res.add(tuple(lst.copy()))
                return
            lst.append(nums[index])
            dfs(index + 1, nums, lst, res)
            lst.pop(len(lst) - 1)
            dfs(index + 1, nums, lst, res)
        dfs(0, nums, lst, res)
        res = [list(x) for x in res]
        return list(res)

nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))
