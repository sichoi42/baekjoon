import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	dp = [0] * n
	dp[0] = 1
	answer = dp[0]
	for i in range(1, n):
		candi = [0]
		for j in range(i):
			if a[i] < a[j]:
				candi.append(dp[j])
		dp[i] = max(candi) + 1
		if dp[i] > answer:
			answer = dp[i]
	print(answer)
