import math

def find_col(map, perfect_num):
	for s in map:
		num = int(s)
		if (math.sqrt(num) - int(math.sqrt(num))) == 0.0 and num != 0:
			perfect_num.append(num)
	return perfect_num

def find_row(n, m, map, perfect_num):
	for i in range(m):
		s = ''
		s = s.join([map[j][i] for j in range(n)])
		num = int(s)
		if (math.sqrt(num) - int(math.sqrt(num))) == 0.0 and num != 0:
			perfect_num.append(num)
	return perfect_num

def perfect_square():
	size = input().split(' ')
	n = int(size[0])
	m = int(size[1])
	map = []
	for i in range(n):
		map.append(input())
	perfect_num = []
	if n < m:
		perfect_num = find_col(map, perfect_num)
		if perfect_num != []:
			return max(perfect_num)
		perfect_num = find_row(n, m, map, perfect_num)
		if perfect_num != []:
			return max(perfect_num)

if __name__ == '__main__':
	result = perfect_square()
	print(result)
