from collections import deque

n, m = map(int, input().split(' '))
maze = [list(map(int, list(input()))) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
queue = deque([[0, 0]])
while queue:
	r, c = queue.popleft()
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if (nr >= 0 and nr < n) and (nc >= 0 and nc < m):
			if maze[nr][nc] == 1:
				queue.append([nr, nc])
				maze[nr][nc] = maze[r][c] + 1
print(maze[n - 1][m - 1])
