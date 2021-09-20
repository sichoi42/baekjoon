from collections import defaultdict

def dfs(v):
	visited[v] = True
	result.append(v)
	for w in graph[v]:
		if visited[w] == False:
			dfs(w)

n = int(input())
e = int(input())
graph = defaultdict(list)
for _ in range(e):
	v1, v2 = map(int, input().split(' '))
	graph[v1].append(v2)
	graph[v2].append(v1)
visited = defaultdict(bool)
result = []
dfs(1)
print(len(result) - 1)
