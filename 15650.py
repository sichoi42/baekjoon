import sys

input = sys.stdin.readline

n, m = map(int, input().split())
entry = []

def dfs(start):
	if len(entry) == m:
		print(' '.join((map(str, entry))))
		return
	for i in range(start, n + 1):
		entry.append(i)
		dfs(i + 1)
		entry.pop()

dfs(1)
