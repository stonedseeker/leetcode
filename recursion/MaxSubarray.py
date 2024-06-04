from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def dfs(index, nums, lst, res):
            if index == len(nums):
                res.append(lst.copy())
                return

            lst.append(nums[index])
            # print(lst)
            dfs(index + 1, nums, lst, res)

                
        return -1
lst = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(lst))









#     list.pop(len(lst) - 1)
        # 
        #     dfs(index + 1, nums, lst, res)
        # 
        # res = []
        # lst = []
        # dfs(0, nums, lst , res)
        # print(res) 
        # # mx = 0
        # maxArr = []
        # # for i in res:
        # #     if sum(i) == 12:
        # #         print(i)
        # 
        # mx = 0
        # for i in res:
        #     mx = max(sum(i), mx)
        #     maxArr = i
        #     print(mx, maxArr, end='\t')
        # print(maxArr, mx, end='\t')
        # return mx

