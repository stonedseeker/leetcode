'''
You are given a 

'''


from typing import List

class Solution:
    def evenOdd(self, nums: List[int])->int:
        l = 0
        max_len = curr_len = 0
    
        for l in range(len(nums)):
            for r in range(1, len(nums)):
                if (nums[l] + nums[r]) % 2 == 1:
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                else:
                    curr_len = 0
                    r += 1

        return max_len



nums = [10, 12, 14, 7, 8]

print(Solution().evenOdd(nums))
