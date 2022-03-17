import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
leng = [False] * n
slsh = [False] * (2 * n - 1)
bckslsh = [False] * (2 * n - 1)

def n_queen(r):
	if r == n:
		global cnt
		cnt += 1
	else:
		for c in range(n):
			if not leng[c] and not slsh[r + c] and not bckslsh[r - c + n - 1]:
				leng[c] = slsh[r + c] = bckslsh[r - c + n - 1] = True
				n_queen(r + 1)
				leng[c] = slsh[r + c] = bckslsh[r - c + n - 1] = False
n_queen(0)
print(cnt)
