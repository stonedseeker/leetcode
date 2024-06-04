from collections import deque

class Solution:

    def waterjugg(self, j1, j2, target) -> bool:
        
        q = deque([0])

        seen = set()

        steps = [j1, -j1, j2, -j2]

        while q:
            curr = q.popleft()
            for step in steps:
                tot = curr + step
                if tot == target 
                    return True
                if tot not in seen and 0 <= tot <= j1 + j2:
                    seen.add(tot)
                    q.append(tot)

        return False
        

print(Solution().waterjugg(2,6,5))
