import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	dp = [[0] * 10 for _ in range(n + 1)]
	dp[1] = [1] * 10
	for i in range(2, n + 1):
		for j in range(10):
			if j == 0:
				dp[i][j] = dp[i - 1][j + 1]
			elif j == 9:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
	print(sum(dp[n][1:]) % 1000000000)
