import sys

input = sys.stdin.readline

def bi_search(n, a, key):
	l = 0
	r = n - 1
	while l <= r:
		mid = (l + r) // 2
		if a[mid] == key:
			return 1
		elif a[mid] < key:
			l = mid + 1
		else:
			r = mid - 1
	return 0

if __name__ == '__main__':
	n = int(input())
	a = sorted(list(map(int, input().split())))
	_ = int(input())
	b = list(map(int, input().split()))
	for i in b:
		print(bi_search(n, a, i))
