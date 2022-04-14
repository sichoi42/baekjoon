import sys

input = sys.stdin.readline

def star(lst, n):
	if n == 1:
		print('\n'.join(lst))
		return
	tmp = lst
	lst = []
	len_tmp = len(tmp)
	for i in range(len_tmp):
		lst.append(tmp[i] * 3)
	for i in range(len_tmp):
		lst.append(tmp[i] + ' ' * len_tmp + tmp[i])
	for i in range(len_tmp):
		lst.append(tmp[i] * 3)
	star(lst, n // 3)

if __name__ == '__main__':
	n = int(input())
	star(['***','* *', '***'], n // 3)
