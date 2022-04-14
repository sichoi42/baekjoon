import sys

input = sys.stdin.readline

n, m = map(int, input().split())
entry = []

def dfs(depth):
	if len(entry) == m:
		print(' '.join(map(str, entry)))
		return
	for i in range(1, n + 1):
		entry.append(i)
		dfs(depth)
		entry.pop()

dfs(1)
