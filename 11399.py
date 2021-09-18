n = int(input())
p = list(map(int, input().split(' ')))

total = 0
result = []
while p != []:
	m = min(p)
	p.remove(m)
	total += m
	result.append(total)
print(sum(result))
