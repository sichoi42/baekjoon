n = int(input())

total = 0
for i in range(5, n + 5, 5):
	if n - i >= 0:
		cnt = 0
		tmp = i
		while tmp != 0:
			if tmp % 5 == 0:
				tmp //= 5
				cnt += 1
			else:
				break
		total += cnt
print(total)
