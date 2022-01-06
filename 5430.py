import sys
from collections import deque
t = int(input())
for __ in range(t):
	ac = sys.stdin.readline().rstrip()
	n = int(input())
	tmp = sys.stdin.readline().rstrip()[1:-1].split(',')
	queue = deque()
	if n > 0:
		for i in range(n):
			queue.append(int(tmp[i]))
	cnt_R = 0
	error = False
	vector = 1
	for c in ac:
		if c == 'R':
			vector *= -1
		elif c == 'D':
			if len(queue) == 0:
				print('error')
				error = True
				break
			if vector == 1:
				queue.popleft()
			else:
				queue.pop()
			n -= 1
	if error == True:
		continue
	print('[', end='')
	if vector == 1:
		for i in range(n):
			if i == n - 1:
				print(queue[i], end='')
			else:
				print(queue[i], end=',')
	else:
		for i in range(n - 1, -1, -1):
			if i == 0:
				print(queue[i], end='')
			else:
				print(queue[i], end=',')
	print(']')
