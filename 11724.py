from collections import defaultdict, deque
import sys

n, m = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(m):
	u ,v = map(int, sys.stdin.readline().split(' '))
	graph[u].append(v)
	graph[v].append(u)
visited = defaultdict(bool)
queue = deque()
cnt = 0
for key in graph.keys():
	if visited[key] == False:
		queue.append(key)
		while queue:
			v = queue.popleft()
			if visited[v] == False:
				visited[v] = True
				for w in graph[v]:
					queue.append(w)
		cnt += 1
print(n - len(graph.keys()) + cnt)
