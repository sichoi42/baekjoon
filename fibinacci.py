def fibo(n):
	a = 1
	b = 1
	c = 2
	for i in range(n - 3):
		a = b
		b = c
		c = a + b
	return c

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		if n == 0:
			print(1, 0)
		elif n == 1:
			print(0, 1)
		elif n == 2:
			print(1, 1)
		elif n == 3:
			print(1, 2)
		else:
			print(fibo(n - 1), end=' ')
			print(fibo(n))
