class Solution:
    def ceil(self, nums, target):
        l, r = 0, len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return r

nums = [2,3,4,5,9,14,16,18]
print(Solution().ceil(nums, 15))
