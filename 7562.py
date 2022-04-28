import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, -2, -2, -1, +1, +2, +2, +1]
dc = [-2, -1, +1, +2, -2, -1, +1, +2]

if __name__ == '__main__':
	for _ in range(int(input())):
		n = int(input())
		start_r, start_c = map(int, input().split())
		end_r, end_c = map(int, input().split())
		visited = [[-1 for _ in range(n)] for _ in range(n)]
		queue = deque()
		visited[start_r][start_c] = 0
		queue.append((start_r, start_c))
		while queue:
			r, c = queue.popleft()
			if r == end_r and c == end_c:
				break
			for k in range(8):
				nr = r + dr[k]
				nc = c + dc[k]
				if 0 <= nr < n and 0 <= nc < n:
					if visited[nr][nc] == -1:
						queue.append((nr, nc))
						visited[nr][nc] = visited[r][c] + 1
		print(visited[end_r][end_c])
