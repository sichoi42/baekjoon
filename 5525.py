import sys

n = int(input())
m = int(input())
s = sys.stdin.readline().rstrip()

p = 'I'
p += n * 'OI'
cnt = 0
ioi = 0
i = 1
while i < m - 1:
	if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
		ioi += 1
		if ioi == n:
			cnt += 1
			ioi -= 1
		i += 1
	else:
		ioi = 0
	i += 1
print(cnt)
