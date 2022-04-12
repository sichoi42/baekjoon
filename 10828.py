import sys

input = sys.stdin.readline

if __name__ == '__main__':
	stack = []
	len_s = 0
	for _ in range(int(input())):
		tmp = input().rstrip()
		try:
			op, num = tmp.split()
		except:
			op = tmp
		if op == 'push':
			stack.append(num)
			len_s += 1
		elif op == 'pop':
			if stack:
				print(stack.pop())
				len_s -= 1
			else:
				print(-1)
		elif op == 'size':
			print(len_s)
		elif op == 'empty':
			if not stack:
				print(1)
			else:
				print(0)
		else:
			if stack:
				print(stack[-1])
			else:
				print(-1)
