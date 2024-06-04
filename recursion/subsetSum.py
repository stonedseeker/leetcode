class Solution:
    def isSubsetSum12 (self, N, nums, summation):
        
        def dfs(index, nums, lst, res):
            if index == len(nums):
                res.append(lst.copy())
                return
            
            lst.append(nums[index])
            dfs(index + 1, nums, lst, res)
            lst.pop()
            dfs(index + 1, nums, lst, res)
        lst = []
        res = []
        dfs(0, nums, lst, res)
        
        sums = []

        for subset in res:
            sum = 0
            for i in subset:
                sum += i
            if sum == summation:
                return True
            
        return False

n = 6
sets = [3, 34, 4, 12, 5, 2]
def isSubsetSum (N, nums, summation):
        
    def dfs(index, target, nums):
        if target == 0:
            return True
        if index == N:
            return False
            
        if nums[index] <= target:
            if dfs(index + 1, target - nums[index], nums):
                return True

        return dfs(index + 1, target, nums)
        
    return dfs(0, summation, nums)


print(isSubsetSum(6, sets, 9))
