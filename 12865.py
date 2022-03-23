import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n, k = map(int, input().split())
	have = [tuple(map(int, input().split())) for _ in range(n)]
	dp = [[0 for _ in range(k + 1)] for _ in range(n)]
	w, v = have[0][0], have[0][1]
	for j in range(k + 1):
		if j >= w:
			dp[0][j] = v
	for i in range(1, n):
		w, v = have[i][0], have[i][1]
		for j in range(k + 1):
			if j >= w:
				dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	print(dp[n - 1][k])
