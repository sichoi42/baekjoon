from collections import deque
import sys

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(visited, ripe_tomato):
	queue = deque()
	for tup in ripe_tomato:
		queue.append(tup)
	while queue:
		r, c = queue.popleft()
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
				queue.append((nr, nc))
				visited[nr][nc] = visited[r][c] + 1
	max = -1
	for r in range(n):
		row_max = -1
		for c in range(m):
			cur = visited[r][c]
			if cur == 0:
				return -1
			elif cur > row_max:
				row_max = cur
		if row_max > max:
			max = row_max
	if max == -1:
		return -1
	else:
		return max - 1

if __name__ == '__main__':
	m, n = map(int, input().split())
	visited = [[0 for _ in range(m)] for _ in range(n)]
	box = []
	ripe_tomato = []
	for r in range(n):
		tmp = list(map(int, input().split()))
		for c in range(m):
			if tmp[c] == 1:
				ripe_tomato.append((r, c))
				visited[r][c] = 1
			elif tmp[c] == -1:
				visited[r][c] = -1
		box.append(tmp)
	print(bfs(visited, ripe_tomato))
