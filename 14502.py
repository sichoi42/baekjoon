import sys
import copy
from collections import deque

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

def simulation(map, virus):
	queue = deque()
	for coord in virus:
		queue.append(coord)
	while queue:
		r, c = queue.popleft()
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nr < n and 0 <= nc < m:
				if map[nr][nc] == 0:
					queue.append((nr, nc))
					map[nr][nc] = 2
	cnt = 0
	for i in range(n):
		for j in range(m):
			if map[i][j] == 0:
				cnt += 1
	global result
	if cnt > result:
		result = cnt

def build_wall(start, cnt, map, virus):
	if cnt == 3:
		simulation(copy.deepcopy(map), virus)
		return
	for i in range(start, n * m):
		r = i // m
		c = i % m
		if map[r][c] == 0:
			map[r][c] = 1
			build_wall(start + 1, cnt + 1, map, virus)
			map[r][c] = 0

if __name__ == '__main__':
	n, m = map(int, input().split())
	map = [list(map(int, input().split())) for _ in range(n)]
	virus = [(i, j) for i in range(n) for j in range(m) if map[i][j] == 2]
	build_wall(0, 0, map, virus)
	print(result)
