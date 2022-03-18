import sys
from collections import defaultdict, deque

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	dic = defaultdict(set)
	ans = defaultdict(int)
	for _ in range(n - 1):
		k, v = map(int, input().split())
		dic[k].add(v)
		dic[v].add(k)
	queue = deque()
	queue.append(1)
	while queue:
		v = queue.popleft()
		for i in dic[v]:
			if v in dic[i]:
				ans[i] = v
				dic[i].remove(v)
			queue.append(i)
	for i in range(2, n + 1):
		print(ans[i])
