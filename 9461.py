t = int(input())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5]
dp = [0 for _ in range(101)]
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
for _ in range(t):
	n = int(input())
	if n > 8:
		for i in range(9, n + 1):
			dp[i] = dp[i - 5] + dp[i - 1]
	print(dp[n])