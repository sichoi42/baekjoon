n = int(input())

cnt = 0
result = []

def hanoi(n, from_, assi, to):
	global cnt
	if n == 1:
		result.append((from_, to))
		cnt += 1
		return
	hanoi(n - 1, from_, to, assi)
	result.append((from_, to))
	cnt += 1
	hanoi(n - 1, assi, from_, to)

hanoi(n, 1, 2, 3)
print(cnt)
for t in result:
	print(*t)
