from typing import List

class Solution:
    def carFleet(self, target: int, pos: List[int], spd: List[int]) -> int:

        pair = [[s,p] for s,p in zip(pos, spd)]
        print(pair)
        stack = []
        
        
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


            

        return 0



pos = [10,8,0,5,3]
spd = [2,4,1,1,3]
print(Solution().carFleet(12, pos, spd))
        
