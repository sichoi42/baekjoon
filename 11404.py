import sys
input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	m = int(input())
	cost = [[float('inf') if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]
	for _ in range(m):
		a, b, c = map(int, input().split())
		if c < cost[a][b]:
			cost[a][b] = c
	for k in range(1, n + 1):
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				if cost[i][k] + cost[k][j] < cost[i][j]:
					cost[i][j] = cost[i][k] + cost[k][j]
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			tmp = cost[i][j]
			if tmp == float('inf'):
				print(0, end=' ')
			else:
				print(tmp, end=' ')
		print()
