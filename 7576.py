from collections import deque

m, n = map(int, input().split(' '))
box = [list(map(int, input().split(' '))) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = deque([])
for i in range(n):
	for j in range(m):
		if box[i][j] == 1:
			queue.append([i, j])
			box[i][j] = -2
day = 1
while queue:
	qsize = len(queue)
	for _ in range(qsize):
		r, c = queue.popleft()
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nr < n and 0 <= nc < m:
				if box[nr][nc] == 0:
					queue.append([nr, nc])
					box[nr][nc] = day
	day += 1
total = 0
for line in box:
	if 0 in line:
		total = -1
		break
if total == 0:
	result = []
	for line in box:
		result.append(max(line))
	total = max(result)
	if total == -1:
		total = 0
print(total)
