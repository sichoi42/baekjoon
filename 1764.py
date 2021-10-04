import sys

n, m = map(int, sys.stdin.readline().split(' '))
no_hear = set()
no_see = set()
for _ in range(n):
	no_hear.add(sys.stdin.readline().rstrip('\n'))
for _ in range(m):
	no_see.add(sys.stdin.readline().rstrip('\n'))
both = no_hear & no_see
print(len(both))
for name in sorted(no_hear & no_see):
	print(name)