from collections import deque

t = int(input())
for l in range(t):
	m, n, k = map(int, input().split(' '))
	field = [[0 for i in range(m)] for j in range(n)]
	for _ in range(k):
		c, r = map(int, input().split(' '))
		field[r][c] = 1
	dr = [-1, 1, 0, 0]
	dc = [0, 0, -1, 1]
	cnt = 0
	for i in range(n):
		for j in range(m):
			if field[i][j] == 1:
				queue = deque([[i, j]])
				cnt += 1
				field[i][j] = 0
				while queue:
					r, c = queue.popleft()
					for k in range(4):
						nr = r + dr[k]
						nc = c + dc[k]
						if 0 <= nr < n and 0 <= nc < m:
							if field[nr][nc] == 1:
								queue.append([nr, nc])
								field[nr][nc] = 0
	print(cnt)
