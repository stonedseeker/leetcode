from typing import List

class Solution:
    def minEatingSpeed(self, piles:List[int], h:int)->int:

        min_pile = min(piles)
        print(min_pile)
        k = min_pile
        
            for i in range(len(piles)):
                while(nums[i] != 0):
                    pile[i] = piles[i] - k
                    
            

nums = [3,6,7,11]
h = 8

print(Solution().minEatingSpeed(nums, h))

