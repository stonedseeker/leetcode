class Solution:
    def ifTrip1(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    print(nums[i], nums[j], nums[k], sep=' ')
                    if nums[i] + nums[j] + nums[k] == 0:
                        return True
        return False


    def ifTrip(self, nums):
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    return True
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return False

nums = [0, -1, 2, -3, 1]
print(Solution().ifTrip(nums))



nums = [0, -1, 2, -3, 1]
print(Solution().ifTrip(nums))
