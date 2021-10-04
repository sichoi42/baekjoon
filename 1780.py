import sys

n = int(sys.stdin.readline())
pap = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
cnt = [0, 0, 0]

def division(i, j, len):
	crit = pap[i][j]
	check = False
	for r in range(i, i + len):
		if set([crit]) != set(pap[r][j:j + len]):
			check = True
	if check == True:
		len //= 3
		division(i, j, len)
		division(i, j + len, len)
		division(i, j + 2 * len, len)
		division(i + len, j, len)
		division(i + len, j + len, len)
		division(i + len, j + 2 * len, len)
		division(i + 2 * len, j, len)
		division(i + 2 * len, j + len, len)
		division(i + 2 * len, j + 2 * len, len)
	else:
		cnt[crit] += 1

if __name__ == '__main__':
	division(0, 0, n)
	for i in range(-1, 2):
		print(cnt[i])