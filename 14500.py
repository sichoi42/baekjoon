import sys

n, m = map(int, sys.stdin.readline().rstrip('\n').split(' '))
pap = [list(map(int, sys.stdin.readline().rstrip('\n').split(' '))) for _ in range(n)]
result = []
for r in range(n):
	for c in range(m):
		#긴거
		if c + 3 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r][c + 2] + pap[r][c + 3])
		if r + 3 < n:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 2][c] + pap[r + 3][c])
		#네모
		if r + 1 < n and c + 1 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r + 1][c] + pap[r + 1][c + 1])
		#지그재그
		if r + 2 < n and c + 1 < m:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c + 1] + pap[r + 2][c + 1])
		if r + 2 < n and 0 <= c - 1:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c - 1] + pap[r + 2][c - 1])
		if r + 1 < n and c + 2 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r + 1][c + 1] + pap[r + 1][c + 2])
		if r + 1 < n and 0 <= c - 2:
			result.append(pap[r][c] + pap[r][c - 1] + pap[r + 1][c - 1] + pap[r + 1][c - 2])
		#산
		if r + 1 < n and c + 2 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r + 1][c + 1] + pap[r][c + 2])
		if r + 1 < n and 0 <= c - 1 and c + 1 < m:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c - 1] + pap[r + 1][c + 1])
		if r + 2 < n and c + 1 < m:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c + 1] + pap[r + 2][c])
		if 0 <= r - 1 and r + 1 < n and c + 1 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r + 1][c + 1] + pap[r - 1][c + 1])
		#갈고리
		if r + 2 < n and c + 1 < m:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 2][c] + pap[r + 2][c + 1])
			result.append(pap[r][c] + pap[r][c + 1] + pap[r + 1][c + 1] + pap[r + 2][c + 1])
		if r + 2 < n and 0 <= c - 1:
			result.append(pap[r][c] + pap[r][c - 1] + pap[r + 1][c - 1] + pap[r + 2][c - 1])
		if 0 <= r - 2 and c + 1 < m:
			result.append(pap[r][c] + pap[r][c + 1] + pap[r - 1][c + 1] + pap[r - 2][c + 1])
		if r + 1 < n and c + 2 < m:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r][c + 1] + pap[r][c + 2])
			result.append(pap[r][c] + pap[r][c + 1] + pap[r][c + 2] + pap[r + 1][c + 2])
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c + 1] + pap[r + 1][c + 2])
		if r + 1 < n and 0 <= c - 2:
			result.append(pap[r][c] + pap[r + 1][c] + pap[r + 1][c - 1] + pap[r + 1][c - 2])
print(max(result))