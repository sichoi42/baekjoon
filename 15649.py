import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n + 1)
entry = []

def dfs(depth):
	if len(entry) == m:
		print(' '.join(map(str, entry)))
		return
	for i in range(1, n + 1):
		if not visited[i]:
			visited[i] = True
			entry.append(i)
			dfs(depth + 1)
			entry.pop()
			visited[i] = False

dfs(1)
