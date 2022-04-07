import sys
from collections import deque

input = sys.stdin.readline

def difussing(room):
	while queue:
		r, c, w = queue.popleft()
		nw = w // 5
		cnt = 0
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nr < R and 0 <= nc < C:
				if room[nr][nc] != -1:
					room[nr][nc] += nw
					cnt += 1
		room[r][c] -= nw * cnt

def cleaning(room):
	up, down = cleaner
	c = 0
	for r in range(up - 1, 0, -1):
		room[r][c] = room[r - 1][c]
	for r in range(down + 1, R - 1):
		room[r][c] = room[r + 1][c]

	r = 0
	for c in range(0, C - 1):
		room[r][c] = room[r][c + 1]
		room[R - 1][c] = room[R - 1][c + 1]

	c = C - 1
	for r in range(0, up):
		room[r][c] = room[r + 1][c]
	for r in range(R - 1, down, -1):
		room[r][c] = room[r - 1][c]

	r = up
	for c in range(C - 1, 0, -1):
		room[r][c] = room[r][c - 1]
		room[r + 1][c] = room[r + 1][c - 1]
	room[r][c] = room[r + 1][c] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

for _ in range(T):
	dust = {}
	queue = deque()
	cleaner = []
	for r in range(R):
		for c in range(C):
			w = room[r][c]
			if w > 4:
				queue.append((r, c, w))
			elif w == -1:
				cleaner.append(r)
	difussing(room)
	cleaning(room)

print(sum([sum(lst) for lst in room]) + 2)
