import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	tree = []
	dp = []
	for i in range(n):
		tmp = list(map(int, input().split()))
		tree.append(tmp)
		dp.append(tmp)
	if n == 1:
		print(tree[0][0])
		sys.exit(0)
	dp[1][0] += tree[0][0]
	dp[1][1] += tree[0][0]
	for i in range(2, n):
		for j in range(i + 1):
			if j == 0:
				dp[i][j] += dp[i-1][j]
			elif i == j:
				dp[i][j] += dp[i-1][j-1]
			else:
				dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
	print(max(dp[n-1]))
