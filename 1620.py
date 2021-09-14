import sys
n, m = map(int, input().split(' '))

name_to_num = {sys.stdin.readline().rstrip():i+1 for i in range(n)}
num_to_name = dict(zip(name_to_num.values(), name_to_num.keys()))
for i in range(m):
	idx = sys.stdin.readline().rstrip()
	try:
		idx = int(idx)
	except:
		pass
	if isinstance(idx, str):
		print(name_to_num[idx])
	elif isinstance(idx, int):
		print(num_to_name[idx])
