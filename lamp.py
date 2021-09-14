import sys

def get_max_on_row(table, k):
	count = dict()
	for key in table:
		try:
			count[key] += 1
		except:
			count[key] = 1
	while (count != {}):
		max_str = max(count, key=count.get)
		if k >= max_str.count('0'):
			if k % 2 == max_str.count('0') % 2:
				return count[max_str]
		count.pop(max_str)
	return 0

def turn_lamp(n, m):
	table = [sys.stdin.readline() for _ in range(n)]
	k = int(input())
	print(get_max_on_row(table, k))

if __name__ == '__main__':
	n, m = map(int, input().split(' '))
	turn_lamp(n, m)
