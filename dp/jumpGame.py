from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1,-1):
            if nums[i] >= goal - i:
                if i == 0: return True
                else: 
                    goal -= 1
                    i -= 1

        
        return False


print(Solution().canJump([3,2,1,0,4]))
