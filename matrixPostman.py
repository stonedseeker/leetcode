class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        ans = []
        dx1 = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy1 = [0, 1, 1, 1, 0, -1, -1, -1]
        dx2 = [-2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2, 2, 2, 1, 0, -1]
        dy2 = [-2, -1, 0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2]

        for i in range(q):
            x, y = queries[i][1], queries[i][2]
            total_sum = 0

            if queries[i][0] == 1:
                for idx in range(8):
                    x_index, y_index = x + dx1[idx], y + dy1[idx]
                    if 0 <= x_index < n and 0 <= y_index < m:
                        total_sum += mat[x_index][y_index]
                ans.append(total_sum)
            else:
                for idx in range(16):
                    x_index, y_index = x + dx2[idx], y + dy2[idx]
                    if 0 <= x_index < n and 0 <= y_index < m:
                        total_sum += mat[x_index][y_index]
                ans.append(total_sum)

        return ans

# Example Usage
n, m = 6, 6
mat = [[1, 2, 3, 4, 5, 6], 
       [7, 8, 9, 10, 11, 12], 
       [13, 14, 15, 16, 17, 18], 
       [19, 20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36]]
q = 1
queries = [[2, 3, 2]]

solution = Solution()
print(solution.matrixSum(n, m, mat, q, queries))  # Output: [336]


n, m = 4, 5
mat = [[1, 2, 3, 4, 10], 
       [5, 6, 7, 8, 10], 
       [9, 1, 3, 4, 10], 
       [1, 2, 3, 4, 10]]
q = 2
queries = [
    [1, 0, 1], 
    [2, 0, 1]
]

print(solution.matrixSum(n, m, mat, q, queries))
