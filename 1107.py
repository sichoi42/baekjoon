# import sys

# n = input()
# m = int(input())
# if m == 0 and n != '100':
# 	print(1)
# 	sys.exit(0)
# disable = input().split(' ')
# if n == '100':
# 	print(0)
# 	sys.exit(0)
# able = [str(i) for i in range(10) if str(i) not in disable]
# if able == []:
# 	print(abs(int(n) - 100))
# 	sys.exit(0)
# len_n = len(n)
# print('able set: ', able)
# result = ''
# for i in range(len_n):
# 	diff = [abs(ord(n[i]) - ord(c)) for c in able]
# 	if 0 in diff:
# 		print(diff)
# 		m = min(diff)
# 		min_idx = [j for j, v in enumerate(diff) if v == m]
# 		result += able[min_idx[0]]
# 	else:
# 		r = ['','','','','','']
# 		for j in range(len_n - i - 1):
# 			r[0] += min(able)
# 		for j in range(len_n - i - 1):
# 			r[1] += max(able)
# 		for j in range(len_n - i):
# 			r[2] += min(able)
# 		for j in range(len_n - i):
# 			r[3] += max(able)
# 		for j in range(len_n - i + 1):
# 			r[4] += min(able)
# 		for j in range(len_n - i + 1):
# 			r[5] += min(able)
# 		print('mid result: ', result)
# 		r = [result + c for c in r if c != '']
# 		tmp = [abs(int(c) - int(n)) for c in r]
# 		min_idx = [j for j, v in enumerate(tmp) if v == min(tmp)]
# 		print(r)
# 		result = r[min_idx[0]]
# 		break
# print('jump result: ', result)
# cnt = 0
# if len(result) + abs(int(result) - int(n)) < abs(100 - int(n)):
# 	cnt += len(result)
# 	cnt += abs(int(result) - int(n))
# else:
# 	cnt += abs(100 - int(n))
# print(cnt)


n = int(input())
m = int(input())
if m == 0 and n != 100:
	print(1)
	sys.exit(0)
disable = map(int, input().split(' '))
if n == 100:
	print(0)
	sys.exit(0)
able = [i for i in range(10) if i not in disable]
if able == []:
	print(abs(n - 100))
	sys.exit(0)
len_n = len(str(n))
