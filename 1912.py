import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	dp = [0] * n
	result = dp[0] = a[0]
	for i in range(1, n):
		dp[i] = max(dp[i - 1] + a[i], a[i])
		result = max(result, dp[i])
	print(result)
