from collections import deque

n = int(input())
map = [list(map(int, list(input()))) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
group = []
for i in range(n):
	for j in range(n):
		if map[i][j] == 1:
			queue = deque([[i, j]])
			group_cnt = 0
			map[i][j] = 0
			while queue:
				r, c = queue.popleft()
				group_cnt += 1
				for k in range(4):
					nr = r + dr[k]
					nc = c + dc[k]
					if 0 <= nr < n and 0 <= nc < n:
						if map[nr][nc] == 1:
							queue.append([nr, nc])
							map[nr][nc] = 0
			group.append(group_cnt)
group.sort()
print(len(group))
for i in group:
	print(i)
