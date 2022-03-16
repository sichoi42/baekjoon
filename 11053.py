import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	dp = [0] * n
	dp[0] = 1
	answer = 1
	for i in range(1, n):
		candidate = [0]
		for j in range(0, i):
			if a[i] > a[j]:
				candidate.append(dp[j])
		dp[i] = max(candidate) + 1
		if dp[i] > answer:
			answer = dp[i]
	print(answer)
