from typing import List
import math

class Solution:
    
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        l = 1
        r = max(nums)
        ans = 0

        while l <= r :
            mid = (l + r) >> 1
            req_tm = self.reqTm(nums, mid)
            print(req_tm)
            if req_tm <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


    def reqTm(self, nums, m):
        res = 0
        for i in range(len(nums)):
            res += math.ceil(nums[i] / m)
        
        print("res = ", res, " m = ", m)
        return res

nums = [3,6,7,11]
h = 8
nums = [30,11,23,4,20]
h = 5

print(Solution().minEatingSpeed(nums, h))

