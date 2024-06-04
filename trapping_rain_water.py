from typing import List

class Solution:
    
    def trap(self, height:List[int]) -> int:
        max_L = 0
        max_R = 0
        l,r = 0, 0

        
        return 0

    def trapSlow(self, height: List[int]):
       left_max = [0] 
       right_max = [0]
       l_m = 0
       r_m = 0

       for i in range(len(height) - 1):
           if height[i] > l_m:
               l_m = height[i]
           left_max.append(l_m)

       for i in range(len(height) - 1):
           if height[i] > r_m:
               r_m = height[i]
           right_max.append(r_m)
           print(i, " ",  r_m)

       right_max = reversed(right_max)

       right_max = list(right_max)
       # right_max[len(right_max) - 1] = height[len(height) - 1]
       right_max.pop(0)
       return left_max, right_max 
       # res = [0] * len(height)
       # i, j = 0, 0
       #
       # for i in range(len(height)):
       #     res[i] = min(left_max[i], right_max[i]) - height[i]
       #
       # count = 0
       # for i in res:
       #      if i > 0:
       #          count += i
       #
       # return count

           


'''
0 1 0 2 1 0 1 3 2 1 2 1 
0 0 1 1 2 2 2 2 3 3 3 3
3 3 3 3 3 3 3 2 2 2 1 0
3 3 3 3 3 3 3 3 2 2 2 1 0
'''


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trapSlow(height))
