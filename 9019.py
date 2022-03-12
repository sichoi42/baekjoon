from collections import deque
import sys

input = sys.stdin.readline

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		a, b = map(int, input().rstrip().split())
		queue = deque()
		queue.append((a, ''))
		visited = set()
		while queue:
			cur, op = queue.popleft()
			visited.add(cur)
			if cur == b:
				print(op)
				break
			next = (2 * cur) % 10000
			if next not in visited:
				queue.append((next, op + 'D'))
				visited.add(next)

			next = (cur - 1) % 10000
			if next not in visited:
				queue.append((next, op + 'S'))
				visited.add(next)

			next = (cur % 1000) * 10 + (cur // 1000)
			if next not in visited:
				queue.append((next, op + 'L'))
				visited.add(next)

			next = (cur // 10) + (cur % 10) * 1000
			if next not in visited:
				queue.append((next, op + 'R'))
				visited.add(next)
