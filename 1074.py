import sys

cnt = 0

def search_z(cur_r, cur_c, n, r, c):
	if n == 0:
		global cnt
		if cur_r == r and cur_c == c:
			print(cnt)
			sys.exit(0)
		else:
			cnt += 1
	else:
		if r >= cur_r and r <= (cur_r + 2**(n - 1) - 1):
			if c >= cur_c and c <= (cur_c + 2**(n - 1) - 1):
				search_z(cur_r, cur_c, n - 1, r, c)
			else:
				cnt += 2**(n-1) * 2**(n-1)
				search_z(cur_r, cur_c + 2**(n - 1), n - 1, r, c)
		else:
			if c >= cur_c and c <= (cur_c + 2**(n - 1) - 1):
				cnt += 2*(2**(n-1) * 2**(n-1))
				search_z(cur_r + 2**(n - 1), cur_c, n - 1, r, c)
			else:
				cnt += 3*(2**(n-1) * 2**(n-1))
				search_z(cur_r + 2**(n - 1), cur_c + 2**(n - 1), n - 1, r, c)

if __name__ == '__main__':
	n, r, c = map(int, input().split(' '))
	if r >= 0 and r <= (2**(n - 1) - 1):
		if c >= 0 and c <= (2**(n - 1) - 1):
			search_z(0, 0, n - 1, r, c)
		else:
			cnt += 2**(n-1) * 2**(n-1)
			search_z(0, 2**(n - 1), n - 1, r, c)
	else:
		if c >= 0 and c <= (2**(n - 1) - 1):
			cnt += 2*(2**(n-1) * 2**(n-1))
			search_z(2**(n - 1), 0, n - 1, r, c)
		else:
			cnt += 3*(2**(n-1) * 2**(n-1))
			search_z(2**(n - 1), 2**(n - 1), n - 1, r, c)

