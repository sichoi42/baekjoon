import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
entry = []

def dfs(depth):
	if len(entry) == m:
		print(' '.join(map(str, entry)))
		return
	for i in range(depth, n):
		entry.append(s[i])
		dfs(i)
		entry.pop()

dfs(0)
