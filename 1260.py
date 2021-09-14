from collections import deque

n, m, v = map(int, input().split(' '))
graph = {i:[] for i in range(1, (n + 1))}
for _ in range(m):
	v1, v2 = map(int, input().split(' '))
	graph[v1].append(v2)
	graph[v2].append(v1)
for key in graph:
	graph[key].sort()
visited = []
stack = [v]
while (stack):
	node = stack.pop()
	if node not in visited:
		visited.append(node)
		stack += reversed(graph[node])
print(' '.join(list(map(str, visited))))

visited = []
queue = deque([v])
while queue:
	node = queue.popleft()
	if node not in visited:
		visited.append(node)
		queue += graph[node]
print(' '.join(list(map(str, visited))))
