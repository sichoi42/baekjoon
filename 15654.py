import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
result = []
visited = {i: False for i in range(n)}

def dfs(depth):
	if depth == m:
		print(' '.join(map(str, result)))
		return
	for i in range(n):
		if not visited[i]:
			visited[i] = True
			result.append(a[i])
			dfs(depth + 1)
			visited[i] = False
			result.pop()

dfs(0)
