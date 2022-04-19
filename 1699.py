import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	dp = [i for i in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, i):
			sqr = j * j
			if sqr > i:
				break
			if dp[i] > dp[i - sqr] + 1:
				dp[i] = dp[i - sqr] + 1
	print(dp[n])
