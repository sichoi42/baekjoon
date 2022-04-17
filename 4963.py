import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, +1, +1, +1]
dc = [-1, 0, +1, -1, +1, -1, 0, +1]

if __name__ == '__main__':
	while True:
		m, n = map(int, input().split())
		if n == 0 and m == 0:
			break
		map_ = [list(map(int, input().split())) for _ in range(n)]
		visited = [[False] * m for _ in range(n)]
		cnt = 0
		for i in range(n):
			for j in range(m):
				if not visited[i][j] and map_[i][j] == 1:
					queue = deque()
					queue.append((i, j))
					visited[i][j] = True
					cnt += 1
					while queue:
						r, c = queue.popleft()
						for k in range(8):
							nr = r + dr[k]
							nc = c + dc[k]
							if 0 <= nr < n and 0 <= nc < m:
								if not visited[nr][nc] and map_[nr][nc] == 1:
									visited[nr][nc] = True
									queue.append((nr, nc))
		print(cnt)
