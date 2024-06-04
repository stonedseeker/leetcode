class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dir = {} # val : index
        for i,n in enumerate(nums):
            diff = target - n;
            breakpoint()
            if diff in dir:
                return [dir[diff], i]
            dir[n] = i
        return []

ans = Solution();

print(ans.twoSum([3,4,2], 6))


