from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        m = amount

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        

        for i in range(n + 1):
            dp[i][0] = 1 

        for i in range(1, n+1):
            for j in range(1, m+1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        print(dp)
        return dp[n][m]

    def count(self, coins, amount):
        res = []
        
        def dfs(index, lst, res):
            if index == len(coins):
                if sum(lst) == amount:
                    res.add(lst.copy())
                return
            lst.append(coins[index])
            dfs(index + 1, lst, res)  # Don't include the current coin
            lst.pop()
            dfs(index + 1, lst, res)  # Include the current coin
        res = set()
        dfs(0, [], res)
        print(res)
        return len(res)
print(Solution().count([1,2,3], 4))

coins= [2, 5, 3, 6]
sum = 10 
print(Solution().count(coins, 10))
