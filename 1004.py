import sys

input = sys.stdin.readline

def is_in_circle(cx, cy, r, x, y):
	if ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 < r:
		return True
	return False

if __name__ == '__main__':
	for _ in range(int(input())):
		x1, y1, x2, y2 = map(int, input().split())
		cnt = 0
		for _ in range(int(input())):
			cx, cy, r = map(int, input().split())
			if is_in_circle(cx, cy, r, x1, y1) ^ is_in_circle(cx, cy, r, x2, y2):
				cnt += 1
		print(cnt)
