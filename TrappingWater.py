'''
Given n non-negative integers representing an elevation map where the width of each 
bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by 
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water 
(blue section) are being trapped.
'''

class Solution:
    def trap(self, height: list[int]):
        count = 0
         
        l,r = 0, len(height) - 1

        left_max, right_max = height[l], height[r]


        
        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                count += left_max - height[l]

            else:
                r -= 1
                right_max = max(right_max, height[r])
                count += right_max - height[r]

        return count
            

print(Solution().trap([4,2,0,3,2,5]))
