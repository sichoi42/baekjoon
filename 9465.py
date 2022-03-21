import sys

input = sys.stdin.readline

if __name__ == '__main__':
	for __ in range(int(input())):
		n = int(input())
		zero, one = [list(map(int, input().split())) for _ in range(2)]
		if n > 1:
			zero[1] += one[0]
			one[1] += zero[0]
		for i in range(2, n):
			zero[i] += max(one[i-2], one[i-1])
			one[i] += max(zero[i-2], zero[i-1])
		print(max(zero[n-1], one[n-1]))
