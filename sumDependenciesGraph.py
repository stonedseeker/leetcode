class Solution:
    def sum_dependencies(self, adj, V):
        
        sum = 0
        for i in range(V):
            sum += len(adj[i])
        return sum




adj = [[2, 3], [3], [3], []]
V = 4

print(Solution().sum_dependencies(adj, V))
