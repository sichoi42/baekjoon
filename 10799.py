import sys

input = sys.stdin.readline

if __name__ == '__main__':
	ps = input().rstrip()
	i = 0
	len_ps = len(ps)
	total = 0
	cnt = 0
	while i < len_ps:
		if ps[i] == '(':
			if ps[i + 1] == ')': # 레이저
				total += cnt
				i += 1
			else: # 기둥 시작
				cnt += 1
		else: # 기둥 끝
			total += 1
			cnt -= 1
		i += 1
	print(total)
