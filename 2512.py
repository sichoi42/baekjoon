import sys

input = sys.stdin.readline

def predicting(s, mid):
	result = 0
	for i in s:
		result += min(i, mid)
	return result

if __name__ == '__main__':
	_ = int(input())
	s = sorted(list(map(int, input().split())))
	m = int(input())
	l = 0
	r = s[-1]
	result = 0
	while l <= r:
		mid = (l + r) // 2
		predi = predicting(s, mid)
		if predi <= m:
			if mid > result:
				result = mid
			l = mid + 1
		else:
			r = mid - 1
	print(result)
