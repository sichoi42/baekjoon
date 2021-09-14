n = input()
m = int(input())
if m == 0 and n != '100':
	print(1)
else:
	disable = input().split(' ')
	if n == '100':
		print(0)
	else:
		result = ''
		able = [str(i) for i in range(10)]
		for c in disable:
			able.remove(c)
		if able == []:
			print(abs(int(n) - 100))
			exit(0)
		len_n = len(n)
		for i in range(len_n):
			diff = [abs(ord(n[i]) - ord(c)) for c in able]
			m = min(diff)
			min_idxes = [j for j, v in enumerate(diff) if v == m]
			if i == 0 and m != 0:
				r = ['', '', '', '', '', '']
				for j in range(len_n + 1):
					r[0] += min([c for c in able])
				for j in range(len_n + 1):
					r[1] += max([c for c in able])
				for j in range(len_n):
					r[2] += min([c for c in able])
				for j in range(len_n):
					r[3] += max([c for c in able])
				for j in range(len_n - 1):
					r[4] += min([c for c in able])
				for j in range(len_n - 1):
					r[5] += max([c for c in able])
				r = [c for c in r if c != '']
				print(r)
				result = [abs(int(c) - int(n)) for c in r]
				print(result)
				break
			else:
				if m != 0 and len(min_idxes) > 1 and i != len_n - 1:
					if n[i + 1] < '5':
						result += able[min_idxes[0]]
						for j in range(len_n - (i + 1)):
							result += max(able)
					else:
						result += able[min_idxes[1]]
						for j in range(len_n - (i + 1)):
							result += min(able)
					break
				else:
					result += able[min_idxes[0]]
		cnt = 0
		#print(result)
		if len(result) + abs(int(result) - int(n)) < abs(100 - int(n)):
			cnt += len(result)
			cnt += abs(int(result) - int(n))
		else:
			cnt += abs(100 - int(n))
		print(cnt)
