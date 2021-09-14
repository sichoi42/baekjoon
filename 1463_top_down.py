import sys
sys.setrecursionlimit(10**9)

n = int(input())
dp = [0 for _ in range(n + 1)]
print(dp)
def solve(n):
	if n == 1:
		return 0
	if dp[n] > 0:
		return dp[n]
	r1=200
	r2=200
	r3=200
	r1 = solve(n - 1) + 1
	if n % 2 == 0:
		r2 = solve(n // 2) + 1
	if n % 3 == 0:
		r3 = solve(n // 3) + 1
	dp[n] = min(r1, r2, r3)
	return dp[n]
print(solve(n))

