import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
entry = []

def dfs(depth):
	if len(entry) == m:
		print(' '.join(map(str, entry)))
		return
	prev = -1
	for i in range(depth, n):
		if prev != a[i]:
			entry.append(a[i])
			prev = a[i]
			dfs(i)
			entry.pop()
dfs(0)
