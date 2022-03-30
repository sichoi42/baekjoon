import sys
from collections import deque

input = sys.stdin.readline

def max(queue):
	max_elem = float('-inf')
	max_idx = 0
	for elem, idx in queue:
		if elem > max_elem:
			max_elem, max_idx = elem, idx
	return (max_elem, max_idx)

if __name__ == '__main__':
	for _ in range(int(input())):
		n, m = map(int, input().split())
		documents = list(map(int, input().split()))
		queue = deque()
		for i in range(n):
			queue.append((documents[i], i))
		for i in range(1, n + 1):
			elem = max(queue)
			idx = queue.index(elem)
			if elem[1] == m:
				print(i)
				break
			for j in range(idx + 1):
				if j != idx:
					queue.append(queue.popleft())
				else:
					queue.popleft()
