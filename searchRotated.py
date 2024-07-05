from typing import List

class Solution:
    def search(self, nums:List[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            

            if nums[l] <= nums[mid]:
                # print("above", nums[l], nums[mid], sep = ' ')
                if target > nums[mid] or target < nums[l]:
                     l = mid + 1
                else:
                    r = mid - 1

            else :
                # print("below", nums[l], nums[mid], sep = ' ')
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

nums = [4,5,6,7,0,1,2]
print(Solution().search(nums, 1))
