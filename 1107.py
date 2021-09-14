def check_able(i, able):
	len = 0
	if i == 0:
		if able[0] == True:
			return 1
		else:
			return 0
	while i != 0:
		if able[i % 10] == False:
			return 0
		i //= 10
		len += 1
	return len

def remote():
	n = int(input())
	m = int(input())
	if m == 0 and n != 100:
		print(1)
		return
	disable = list(map(int, input().split(' ')))
	if n == 100:
		print(0)
		return
	able = {i: True for i in range(10)}
	for key in able:
		if key in disable:
			able[key] = False
	cnt = 0
	for v in able.values():
		if v == True:
			cnt += 1
	if cnt == 0:
		print(abs(n - 100))
		return
	cnt = []
	for i in range(1000000):
		len = check_able(i, able)
		if len > 0:
			cnt.append(len + abs(i - n))
	cnt.append(abs(100 - n))
	print(min(cnt))

remote()
