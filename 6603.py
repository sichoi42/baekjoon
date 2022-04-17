import sys

input = sys.stdin.readline

entry = []

def dfs(s, k, depth):
	if len(entry) == 6:
		print(' '.join(map(str, entry)))
		return
	for i in range(depth, k):
		entry.append(s[i])
		dfs(s, k, i + 1)
		entry.pop()

if __name__ == '__main__':
	while True:
		tmp = list(map(int, input().split()))
		k = tmp[0]
		if k == 0:
			break
		s = tmp[1:]
		dfs(s, k, 0)
		print()
