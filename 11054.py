import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	up = [1] * n
	down = [1] * n
	for i in range(1, n):
		up_candi = [0]
		down_candi = [0]
		for j in range(0, i):
			if a[i] > a[j]:
				up_candi.append(up[j])
			if a[n - 1 - i] > a[-j - 1]:
				down_candi.append(down[-j - 1])
		up[i] = max(up_candi) + 1
		down[n - 1 - i] = max(down_candi) + 1
	answer = 1
	for i in range(n):
		tmp = up[i] + down[i] - 1
		if tmp > answer:
			answer = tmp
	print(answer)
