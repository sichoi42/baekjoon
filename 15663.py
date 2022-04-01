import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
entry = []
visited = {i: False for i in range(n)}

def dfs(depth):
	if depth == m:
		print(' '.join(map(str, entry)))
		return
	prev = -1
	for i in range(n):
		if not visited[i] and prev != a[i]:
			visited[i] = True
			entry.append(a[i])
			prev = a[i]
			dfs(depth + 1)
			visited[i] = False
			entry.pop()
dfs(0)
