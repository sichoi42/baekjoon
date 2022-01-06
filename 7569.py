from collections import deque
import sys

m, n, h = map(int, input().split(' '))
box = [[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)] for i in range(h)]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque([])
for k in range(h):
	for i in range(n):
		for j in range(m):
			if box[k][i][j] == 1:
				queue.append([k, i, j])
				box[k][i][j] = -2
day = 1
while queue:
	qsize = len(queue)
	for _ in range(qsize):
		z, r, c = queue.popleft()
		for k in range(6):
			nz = z + dz[k]
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nz < h and 0 <= nr < n and 0 <= nc < m:
				if box[nz][nr][nc] == 0:
					queue.append([nz, nr, nc])
					box[nz][nr][nc] = day
	day += 1
total = 0
for height in box:
	for line in height:
		if 0 in line:
			total = -1
			break
if total == 0:
	result = []
	for height in box:
		for line in height:
			result.append(max(line))
	total = max(result)
	if total == -1:
		total = 0
if total == -2:
	total = 0
print(total)
