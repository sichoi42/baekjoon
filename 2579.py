n = int(input())
stairs = [int(input()) if i != 0 else i for i in range(n + 1)]
dp = [0 for i in range(n + 1)]
dp[1] = stairs[1]
if n >= 2:
	dp[2] = dp[1] + stairs[2]
if n >= 3:
	dp[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])
for i in range(4, n + 1):
	dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
print(dp[n])
