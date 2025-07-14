from typing import List
import heapq

def maximum_path_score_with_teleport(grid: List[List[int]]) -> int:
    def max_path_without_teleport(start_x: int, start_y: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-float('inf')] * n for _ in range(m)]
        dp[start_x][start_y] = grid[start_x][start_y]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        max_heap = []
        heapq.heappush(max_heap, (-dp[start_x][start_y], start_x, start_y))
        
        while max_heap:
            current_score, x, y = heapq.heappop(max_heap)
            current_score = -current_score
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if dp[nx][ny] < current_score + grid[nx][ny]:
                        dp[nx][ny] = current_score + grid[nx][ny]
                        heapq.heappush(max_heap, (-dp[nx][ny], nx, ny))
        
        return max(max(row) for row in dp)

    m, n = len(grid), len(grid[0])
    overall_max = -float('inf')
    
    for i in range(m):
        for j in range(n):
            max_path_score = max_path_without_teleport(i, j)
            for x in range(m):
                for y in range(n):
                    if (i, j) != (x, y):
                        teleport_score = grid[i][j] + grid[x][y]
                        max_path_score_with_teleport = max_path_without_teleport(x, y) + teleport_score
                        overall_max = max(overall_max, max_path_score_with_teleport)
    
    return overall_max


grid = [
    [1, 2],
    [3, 4]
]
assert maximum_path_score_with_teleport(grid) == 12



grid = [
    [1],
    [2],
    [3],
    [4],
    [5]
]
assert maximum_path_score_with_teleport(grid) == 15




grid = [
    [1],
    [2],
    [3],
    [4],
    [5]
]
assert maximum_path_score_with_teleport(grid) == 15



grid = [
    [1, 10, 1],
    [2, 50, 2],
    [3, 4, 5]
]
assert maximum_path_score_with_teleport(grid) == 71

