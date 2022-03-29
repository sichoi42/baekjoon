import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	matrix = [input().rstrip().split() for _ in range(n)]
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if matrix[i][k] == '1' and matrix[k][j] == '1':
					matrix[i][j] = '1'
	for s in matrix:
		print(' '.join(s))
