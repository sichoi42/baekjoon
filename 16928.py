import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
	n, m = map(int, input().split())
	ladders = {x: y for x, y in [map(int, input().split()) for _ in range(n + m)]}

	cnt = [0] * 101
	queue = deque()
	queue.append(1)
	while queue:
		x = queue.popleft()
		for i in range(1, 7):
			next = x + i
			if next > 100:
				continue
			if next in ladders.keys():
				next = ladders[next]
			if cnt[next] == 0:
				cnt[next] = cnt[x] + 1
				queue.append(next)
	print(cnt[100])
