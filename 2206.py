import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(map, visited):
	queue = deque()
	queue.append((0, 0, 0))
	visited[0][0][0] = 1
	while queue:
		r, c, flag = queue.popleft()
		if r == n - 1 and c == m - 1:
			return visited[flag][r][c]
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 <= nr < n and 0 <= nc < m:
				# 인접한 칸이 벽이 아니면서 방문한 적이 없는 경우
				if map[nr][nc] == 0 and visited[flag][nr][nc] == 0:
					queue.append((nr, nc, flag))
					visited[flag][nr][nc] = visited[flag][r][c] + 1
				# 인접한 칸이 벽이면서 벽을 부순적이 없는 경우
				elif map[nr][nc] == 1 and flag == 0:
					# flag를 1로 전달, 벽을 부수고 진행하면 flag=1인 차원에서 bfs가 진행.
					queue.append((nr, nc, 1))
					visited[1][nr][nc] = visited[0][r][c] + 1
	return -1

if __name__ == '__main__':
	n, m = map(int, input().split())
	map = [list(map(int, input().rstrip())) for _ in range(n)]
	visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
	print(bfs(map, visited))
