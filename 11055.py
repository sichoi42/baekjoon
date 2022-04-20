import sys, copy

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	dp = copy.deepcopy(a)
	answer = float('-inf')
	for i in range(1, n):
		candi = 0
		for j in range(i):
			if a[i] > a[j] and dp[j] > candi:
				candi = dp[j]
		dp[i] += candi
		if dp[i] > answer:
			answer = dp[i]
	print(answer)
