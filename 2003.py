import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	sum = 0
	cnt = 0
	e = 0
	for s in range(n):
		while sum < m and e < n:
			sum += a[e]
			e += 1
		if sum == m:
			cnt += 1
		sum -= a[s]
	print(cnt)
