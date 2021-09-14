from collections import deque, defaultdict

n, m, v = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(m):
	v1, v2 = map(int, input().split(' '))
	graph[v1].append(v2)
	graph[v2].append(v1)
for key in graph:
	graph[key].sort()

def dfs(v):
	visited[v] = True
	result.append(v)
	for w in graph[v]:
		if visited[w] == True:
			continue
		dfs(w)

def bfs(v):
	queue = deque([v])
	while queue:
		w = queue.popleft()
		if visited[w] == False:
			visited[w] = True
			result.append(w)
			queue += graph[w]

result = []
visited = defaultdict(bool)
dfs(v)
print(' '.join(list(map(str, result))))
result = []
visited = defaultdict(bool)
bfs(v)
print(' '.join(list(map(str, result))))
