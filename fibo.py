dp = [0 for i in range(1000)]

def fibo_top_down(n):
	if n == 0:
		return 0
	elif n <= 2:
		return 1
	if dp[n] == 0:
		dp[n] = dp(n - 1) + dp(n - 2)
	return dp[n]

def fibo_bottom_up(n):
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n + 1):
		dp[i] = dp[i - 1] + dp[i - 2]
	return dp[n]
print(fibo_bottom_up(100))
