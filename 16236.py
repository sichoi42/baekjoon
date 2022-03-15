import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	space = []
	visited = {}
	for r in range(n):
		tmp = input().rstrip()
		c = tmp.find('9') // 2
		if c > -1:
			shark = (r, c)
		space.append(list(map(int, tmp.split())))
		for c in range(n):
			visited[(r, c)] = False
	dr = [-1, 1, 0, 0]
	dc = [0, 0, -1, 1]
	queue = deque()
	queue.append(shark)
	size = 2
	ate = 0
	time = 0
	sec = 0
	while queue:
		qsize = len(queue)
		candidate = []
		for _ in range(qsize):
			r, c = queue.popleft()
			visited[(r, c)] = True
			for k in range(4):
				nr = r + dr[k]
				nc = c + dc[k]
				if 0 <= nr < n and 0 <= nc < n and not visited[(nr, nc)]:
					if size >= space[nr][nc]:
						visited[(nr, nc)] = True
						if size > space[nr][nc] > 0:
							candidate.append((nr, nc))
						else:
							queue.append((nr, nc))
		time += 1
		if not candidate:
			if not queue:
				print(sec)
		else:
			space[shark[0]][shark[1]] = 0
			shark = sorted(candidate, key=lambda x: (-x[0], -x[1])).pop()
			space[shark[0]][shark[1]] = 9
			visited = {(i, j): False for i in range(n) for j in range(n)}
			queue.clear()
			queue.append(shark)
			ate += 1
			if ate == size:
				size += 1
				ate = 0
			sec += time
			time = 0
