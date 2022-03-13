import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	dp = [0] * (n + 1)
	dp[1] = 1
	for i in range(1, n + 1):
		dp[i] = 1 + dp[i - 1]
		j = 2
		while j * j <= i:
			dp[i] = min(dp[i], 1 + dp[i - j * j])
			j += 1

	print(dp[n])
