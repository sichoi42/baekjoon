import sys

n = int(sys.stdin.readline())
scr = [sys.stdin.readline().rstrip('\n') for _ in range(n)]

result = []
def division(i, j, len):
	crit = scr[i][j]
	check = False
	for r in range(i, i + len):
		if set(crit) != set(scr[r][j:j + len]):
			check = True
	if check == False:
		result.append(crit)
	else:
		result.append('(')
		len //= 2
		division(i, j, len)
		division(i, j + len, len)
		division(i + len, j, len)
		division(i + len, j + len, len)
		result.append(')')
def main():
	division(0, 0, n)
	print(''.join(result))

if __name__ == '__main__':
	main()