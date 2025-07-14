class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        
        
        n = min(len(val), len(wt))
        dp = [[-1 for _ in range(n+1)] for _ in range(capacity + 1)]
        print(dp)
        
        def dfs(index, capacity):

            if dp[capacity][index] != -1:
                return dp[capacity][index]

            if index == n or capacity == 0:
                return 0
            if wt[index] <= capacity:
                
                dp[capacity][index] =  max(val[index] + dfs(index + 1, capacity - wt[index]),dfs(index+1, capacity))
            else:
                dp[capacity][index] = dfs(index + 1, capacity)
            
            print(dp)
            return dp[capacity][index]
            
    
        return dfs(0, capacity)


print(Solution().knapSack(4, [1,2,3], [4,5,1]))
print(Solution().knapSack(5, [10, 40, 30, 50], [5, 4, 6, 3]))
