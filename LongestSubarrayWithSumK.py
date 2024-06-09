class Solution:
    def longest_subarray(self, nums, k):
        l = r = sum = max_len = 0

        while (r < len(nums)):
            sum = sum + nums[r]
            while (sum > k):
                sum -= nums[l]
                l += 1
            if sum <= k:
                max_len = max(max_len, r - l + 1)
            r = r + 1
        return r, l, max_len

nums = [2, 5, 1, 10, 10]
print(Solution().longest_subarray(nums, 14))
