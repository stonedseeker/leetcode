from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        lst = []

        def dfs(index, nums, lst, res):
            if index == len(nums):
                res.add(tuple(lst.copy()))
                print(res)
                return
            lst.append(nums[index])
            dfs(index + 1, nums, lst, res)
            lst.pop(len(lst) - 1)
            dfs(index + 1, nums, lst, res)
        dfs(0, nums, lst, res)
        print(res)
        res = [list(x) for x in res]
        print(res)
        return list(res) 

nums = [1,2,2]
print(Solution().subsetsWithDup(nums))
