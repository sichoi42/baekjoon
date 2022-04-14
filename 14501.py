import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	t, p = [0], [0]
	dp = [0] * (n + 2)
	for _ in range(n):
		ti, pi = map(int, input().split())
		t.append(ti)
		p.append(pi)
	for i in range(1, n + 2):
		for j in range(1, i):
			dp[i] = max(dp[i], dp[j])
			if j + t[j] == i:
				dp[i] = max(dp[i], dp[j] + p[j])
	print(dp[n + 1])
