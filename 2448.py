import sys

input = sys.stdin.readline

small_star = [
	[' ', ' ', '*', ' ', ' '],
	[' ', '*', ' ', '*', ' '],
	['*', '*', '*', '*', '*']
]

def star(n, r, c):
	if n == 3:
		for i in range(n):
			for j in range(2 * n - 1):
				map[r + i][c + j] = small_star[i][j]
		return
	star(n // 2, r, c + n // 2)
	star(n // 2, r + n // 2, c)
	star(n // 2, r + n // 2, c + n)

n = int(input())
map = [[' ' for _ in range(2 * n - 1)] for _ in range(n)]
star(n, 0, 0)
for r in range(n):
	print(''.join(map[r]))
