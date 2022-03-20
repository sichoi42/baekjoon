import sys

input = sys.stdin.readline

def cutting(lans, length):
	total = 0
	for i in lans:
		total += i // length
	return total

if __name__ == '__main__':
	k, n = map(int, input().split())
	lans = [int(input()) for _ in range(k)]
	l = 0
	r = max(lans)
	result = 0
	while l <= r:
		mid = (l + r) // 2
		if mid == 0:
			mid = 1
		cnt = cutting(lans, mid)
		if cnt < n: #길이를 줄이고 개수를 늘림.
			r = mid - 1
		else: #길이를 늘리고 개수를 줄임.
			l = mid + 1
			if mid > result:
				result = mid
	print(result)
