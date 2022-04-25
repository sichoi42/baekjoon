import sys

input = sys.stdin.readline

N, S = map(int, input().split())
s = list(map(int, input().split()))

entry = []

def tree(depth, sum):
	if depth == N:
		if sum == S:
			global cnt
			cnt += 1
		return
	tree(depth + 1, sum)
	tree(depth + 1, sum + s[depth])

cnt = 0
tree(0, 0)
if S == 0:
	cnt -= 1
print(cnt)
