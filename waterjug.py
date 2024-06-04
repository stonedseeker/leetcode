class Solution:

    count = 0

    def willFill(self, j1, j2, target) -> bool:

        global count 
        
        seen = set()
    
        def dfs(tot):
            if tot == target:
                return True
            if tot in seen or tot < 0 or tot > j1 + j2:
                return False
            
            seen.add(tot)
            return dfs(tot + j1) + dfs(tot + j2) + dfs(tot - j1) + dfs(tot - j2)

        return dfs(0)

print(Solution().willFill(1, 2, 3))
