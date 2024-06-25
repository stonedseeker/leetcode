class Solution:
    def dfs(self, nums, i, res, lst):
        
        if i == len(nums):
            res.append(lst.copy())
            return
         
    
        lst.append(nums[i])
        self.dfs(nums, i + 1, res, lst)
        lst.pop(-1)
        self.dfs(nums, i+1, res, lst)


res = []
lst = []

Solution().dfs([1,2,3,4], 0, res, lst)
print(res)


