import sys
from collections import defaultdict

t = int(input())

for _ in range(t):
	n = int(input())
	if n == 0:
		print(0)
		continue
	closet = dict()
	closet = defaultdict(int)
	for __ in range(n):
		closet[sys.stdin.readline().rstrip().split()[1]] += 1
	result = 0
	cnt = 0
	for key in closet.keys():
		if cnt == 0:
			result += closet[key] + 1
		else:
			result *= closet[key] + 1
		cnt += 1
	print(result - 1)
