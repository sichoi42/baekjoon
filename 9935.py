import sys

input = sys.stdin.readline

if __name__ == '__main__':
	s = input().rstrip()
	bomb = input().rstrip()
	result = []
	len_bomb = len(bomb)
	lb_word = bomb[-1]
	for c in s:
		result.append(c)
		if c == lb_word and ''.join(result[-len_bomb:]) == bomb:
			del result[-len_bomb:]
	if not result:
		print('FRULA')
	else:
		print(''.join(result))
