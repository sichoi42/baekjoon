import sys

input = sys.stdin.readline

if __name__ == '__main__':
	s1 = ' ' + input().rstrip()
	s2 = ' ' + input().rstrip()
	len_s1 = len(s1)
	len_s2 = len(s2)
	lcs = [[0 for _ in range(len_s2)] for _ in range(len_s1)]
	for i in range(1, len_s1):
		for j in range(1, len_s2):
			if s1[i] == s2[j]:
				lcs[i][j] = lcs[i - 1][j - 1] + 1
			else:
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
	print(lcs[len_s1 - 1][len_s2 - 1])
