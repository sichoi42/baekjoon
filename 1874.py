import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	stack = []
	offset = 0
	prev = 0
	result = ''
	for _ in range(n):
		now = int(input())
		if now > prev:
			for i in range(prev + 1, prev + now - offset + 1):
				stack.append(i)
				result += '+\n'
				offset += 1
			prev = stack.pop()
			result += '-\n'
		elif now < prev:
			if stack.pop() != now:
				print('NO')
				sys.exit(0)
			result += '-\n'
	print(result)
