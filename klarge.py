from collections import Counter

class Solution:
    def large(self, nums, k):
        
        lst = []

        for _ in range(k):
            lst.append(max(nums))
            nums.remove(max(nums)) 
        
        

        return lst[len(lst) - 1]

nums = [1,2,3,4,5]
print(Solution().large(nums, 4))


