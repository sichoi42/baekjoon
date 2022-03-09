import sys

def gcd(a, b):
	while b != 0:
		r = a % b
		if r == 0:
			return b
		else:
			a = b
			b = r

def lcm(a, b):
	return (int)(a * b / gcd(a, b))

def main():
	t = (int)(input())
	for _ in range(t):
		m, n, x, y = map(int, sys.stdin.readline().split(' '))
		lcm_mn = lcm(m, n)
		while x % n != y % n:
			if x > lcm_mn:
				x = -1
				break
			x += m
		print(x)

if __name__ == '__main__':
	main()
