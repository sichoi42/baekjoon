import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	a = 1
	if n == 1:
		c = a
	else:
		b = 2
		if n >= 3:
			for _ in range(n - 2):
				c = (a + b) % 15746
				a, b = b, c
		else:
			c = b
	print(c)
