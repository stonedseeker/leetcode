class Solution:
    def max_int(self, nums) -> int:
        max = -99999999
        for i in nums:
            if i > max:
                max = i

        return max

nums = [1,2, 3, -4, 2, 5]
print(Solution().max_int(nums))


