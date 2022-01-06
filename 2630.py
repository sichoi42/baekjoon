white = 0
blue = 0

def cutting(pap, n, x, y):
	global white, blue
	b = 0
	w = 0
	for i in range(x, x + n):
		for j in range(y, y + n):
			if pap[i][j] == 0:
				w += 1
			else:
				b += 1
	if w == n ** 2:
		white += 1
	elif b == n ** 2:
		blue += 1
	else:
		cutting(pap, n // 2, x, y)
		cutting(pap, n // 2, x + n // 2, y)
		cutting(pap, n // 2, x, y + n // 2)
		cutting(pap, n // 2, x + n // 2, y + n // 2)

def main():
	n = int(input())
	pap = [list(map(int, list(input().split(' ')))) for _ in range(n)]
	cutting(pap, n, 0, 0)
	print(white, blue, sep='\n')

if __name__ == '__main__':
	main()
