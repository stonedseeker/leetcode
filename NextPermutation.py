from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if (index == -1):
            nums.reverse()
            print(nums)
            return 

            
        for j in range(len(nums) -1, index, -1):
            if nums[j] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        nums[index+1:] = reversed(nums[index+1:])
        print(nums)

nums = [3,2,1]

print(Solution().nextPermutation(nums))


# def permutation(nums):
#             res = []
#             map = {}
#             for i in nums:
#                 map[i] = 0
#
#             def dfs(nums, lst, res, map):
#
#                 if len(lst) == len(nums):
#                     res.append(lst.copy())
#
#                 for i in range(len(nums)):
#                     if nums[i] not in map:
#                         lst.append(nums[i])
#                         map.append(nums[i])
#                         dfs(nums, lst, res, map)
#                         lst.pop()
#                         map.remove(nums[i])
#             dfs(nums, [], res, [])
#
#
#             return list(res)
#
#         res = permutation(nums)
#         print(res)
#
#         for i in range(len(res)):
#             print(nums, res[i], sep=' ')
#             if nums == res[i]:
#                 if i == len(nums) - 1:
#                     nums = res[0]
#                     break
#                 else:
#                     nums = res[i+1]
#                     break
#         print("nums => ", nums)

