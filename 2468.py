import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

if __name__ == '__main__':
	n = int(input())
	map_ = []
	max = 0
	min = 101
	for _ in range(n):
		tmp = list(map(int, input().split()))
		for cur in tmp:
			if cur > max:
				max = cur
			elif cur < min:
				min = cur
		map_.append(tmp)
	h = min - 1
	result = 0
	while h <= max:
		cnt = 0
		visited = [[False] * n for _ in range(n)]
		for i in range(n):
			for j in range(n):
				if not visited[i][j] and map_[i][j] > h:
					visited[i][j] = True
					cnt += 1
					queue = deque()
					queue.append((i, j))
					while queue:
						r, c = queue.popleft()
						for k in range(4):
							nr = r + dr[k]
							nc = c + dc[k]
							if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
								if map_[nr][nc] > h:
									visited[nr][nc] = True
									queue.append((nr, nc))
		if cnt > result:
			result = cnt
		h += 1
	print(result)
