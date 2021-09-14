cnt = 0

def find_z():
	n, r, c = map(int, input().split(' '))
	global cnt
	while n != 0:
		criterial = 2**(n - 1)
		if r < criterial:
			if c >= criterial:
				cnt += criterial * criterial
				c -= criterial
		else:
			r -= criterial
			if c < criterial:
				cnt += 2 * criterial * criterial
			else:
				cnt += 3 * criterial * criterial
				c -= criterial
		n -= 1
	print(cnt)
if __name__ == '__main__':
	find_z()
