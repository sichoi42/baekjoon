import sys

input = sys.stdin.readline

if __name__ == '__main__':
	for _ in range(int(input())):
		ps = input().rstrip()
		cnt = 0
		for c in ps:
			if c == '(':
				cnt += 1
			else:
				cnt -= 1
			if cnt < 0:
				break
		if cnt == 0:
			print('YES')
		else:
			print('NO')
