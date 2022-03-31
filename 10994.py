import sys

input = sys.stdin.readline

def star(n):
	lst = []
	if n == 1:
		return ['*']
	s = 4 * n - 3
	lst.append('*' * s)
	lst.append('*' + ' ' * (s - 2) + '*')
	for c in star(n - 1):
		lst.append('* ' + c + ' *')
	lst.append('*' + ' ' * (s - 2) + '*')
	lst.append('*' * s)
	return lst

if __name__ == '__main__':
	n = int(input())
	print('\n'.join(star(n)))
