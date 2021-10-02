import sys
from collections import deque

n = int(input())
section = [sys.stdin.readline().rstrip('\n') for _ in range(n)]
weak_section = []
for i in range(n):
	weak_section.append(list(section[i].replace('G', 'R')))
	section[i] = list(section[i])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0
for i in range(n):
	for j in range(n):
		if section[i][j] != 'X':
			color = section[i][j]
			section[i][j] = 'X'
			cnt += 1
			queue = deque([[i, j]])
			while queue:
				r, c = queue.popleft()
				for k in range(4):
					nr = r + dr[k]
					nc = c + dc[k]
					if 0 <= nr < n and 0 <= nc < n:
						if section[nr][nc] != 'X' and section[nr][nc] == color:
							section[nr][nc] = 'X'
							queue.append([nr, nc])
weak_cnt = 0
for i in range(n):
	for j in range(n):
		if weak_section[i][j] != 'X':
			color = weak_section[i][j]
			weak_section[i][j] = 'X'
			weak_cnt += 1
			queue = deque([[i, j]])
			while queue:
				r, c = queue.popleft()
				for k in range(4):
					nr = r + dr[k]
					nc = c + dc[k]
					if 0 <= nr < n and 0 <= nc < n:
						if weak_section[nr][nc] != 'X' and weak_section[nr][nc] == color:
							weak_section[nr][nc] = 'X'
							queue.append([nr, nc])
print(cnt, weak_cnt)