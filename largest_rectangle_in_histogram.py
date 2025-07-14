class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack, max_area, n = [], 0, len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                max_area = max(max_area, heights[idx] * (i - (stack[-1] if stack else -1) -1))
            stack.append(i)

        while stack:
            idx = stack.pop()
            max_area = max(max_area, heights[idx] * (n - (stack[-1] if stack else -1) -1))
        return max_area

print(Solution().largestRectangleArea([2,1,5,6,2,3]))
