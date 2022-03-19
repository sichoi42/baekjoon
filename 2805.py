import sys

input = sys.stdin.readline

def is_more_than_m(m, trees, h):
	yields = 0
	for i in trees:
		diff = i - h
		if diff > 0:
			yields += diff
	if yields >= m:
		return True
	return False

if __name__ == '__main__':
	n, m = map(int, input().split())
	trees = list(map(int, input().split()))
	l = 0
	r = max(trees)
	while l <= r:
		mid = (l + r) // 2
		if is_more_than_m(m, trees, mid):
			l = mid + 1
			h = mid
		else:
			r = mid - 1
	print(h)
