tmp = input()
sign = 1
if tmp[0] == '-':
	sign *= -1
	tmp = tmp.split('-')[1:]
else:
	tmp = tmp.split('-')
tmp2 = []
for lst in tmp:
	tmp2.append(list(map(int, lst.split('+'))))
result = 0
result += sign * sum(tmp2[0])
for atom in tmp2[1:]:
	result += -1 * sum(atom)
print(result)
