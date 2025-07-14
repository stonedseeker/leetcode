from typing import List

class Solution:
    def isCyclic(self, V: int, edges: List[List[int]]) -> bool:
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            print(adj)
           
         
        visited = [False] * V
        rec_stack = [False] * V
       
        def dfs(v):
            visited[v] = True
            rec_stack[v] = True
           
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True
           
            rec_stack[v] = False
            return False
        
        # Call DFS for each unvisited vertex
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        
        return False

# Example usage:
sol = Solution()
V = 4
edges = [[0,1], [1,2], [2,3], [3,1]]
print(sol.isCyclic(V, edges))
