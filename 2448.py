import sys

input = sys.stdin.readline

n = int(input())
def star(lst, n):
	if n == 1:
		print('\n'.join(lst))
		return
	tmp = lst
	len_tmp = len(tmp)
	lst = []
	for i in range(len_tmp):
		lst.append(' ' * len_tmp + tmp[i] + ' ' * len_tmp)
	for i in range(len_tmp):
		lst.append(tmp[i] + ' ' + tmp[i])
	star(lst, n // 2)
star(['  *  ', ' * * ', '*****'], n // 3)
