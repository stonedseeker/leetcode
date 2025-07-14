from collections import deque

class Solution:
	def orangesRotting(self, mat):
		#Code here
		m = len(mat)
		n = len(mat[0])
		q = deque()
		fresh = 0
		time = 0
		directions = [(0,1), (1,0), (0,-1), (-1,0)]

		for i in range(m):
			for j in range(n):
				if mat[i][j] == 2:
					q.append((i,j))
				elif mat[i][j] == 1:
					fresh += 1
				else:
					continue

		while q and fresh > 0:
			size = len(q)
			infected = False
			for _ in range(size):
				x, y = q.popleft()
				for dx, dy in directions:
					nx, ny = x + dx, y + dy
					if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
						mat[nx][ny] = 2
						q.append((nx, ny))
						fresh -= 1
						infected = True
			if infected:
				time += 1
		
		if fresh == 0:
			return time
		else:
			return -1
			