import sys, math

input = sys.stdin.readline

def discriminant(x1, y1, r1, x2, y2, r2):
	if x1 == x2 and y1 == y2:
		if r1 == r2:
			return -1
		else:
			return 0
	d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	sum_r = float(r1 + r2)
	sub_r = float(abs(r1 - r2))
	if sum_r == d or sub_r == d:
		return 1
	elif sub_r < d < sum_r:
		return 2
	else:
		return 0

if __name__ == '__main__':
	for _ in range(int(input())):
		x1, y1, r1, x2, y2, r2 = map(int, input().split())
		print(discriminant(x1, y1, r1, x2, y2, r2))
