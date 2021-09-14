tmp = int(input())
start = 3
total = 0
while start > 0:
	n = tmp
	cnt = 0
	while n - start:
		n -= start
		cnt += 1
