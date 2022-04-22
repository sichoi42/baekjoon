import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	if n == 1:
		print(10)
		sys.exit(0)
	dp = [[0] * 10 for _ in range(n + 1)]
	for i in range(10):
		dp[1][i] = 10 - i
	for i in range(2, n + 1):
		for j in range(10):
			dp[i][j] = sum(dp[i - 1][j:]) % 10007
	print(sum(dp[n - 1]) % 10007)
