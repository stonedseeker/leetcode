class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r ) // 2
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


nums = [1,3,5,6,7,8,12,43,54,63,70]
print(Solution().search(nums, 70))
