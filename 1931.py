import sys

n = int(input())
table = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
table = sorted(table, key=lambda x : (x[1], x[0]))

cnt = 1
end = table[0][1]
for i in range(1, n):
	if table[i][0] >= end:
		cnt += 1
		end = table[i][1]
print(cnt)