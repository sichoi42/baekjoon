import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

total = {i for i in range(1, n + 1)}
m = n // 2
result = float('inf')
entry = []

def divide_team(depth):
	if len(entry) == m:
		start_abil = 0
		for start in list(combinations(entry, 2)):
			r, c = start
			start_abil += graph[r-1][c-1] + graph[c-1][r-1]
		link_abil = 0
		for link in list(combinations(total - set(entry), 2)):
			r, c = link
			link_abil += graph[r-1][c-1] + graph[c-1][r-1]
		diff = abs(start_abil - link_abil)
		global result
		if diff < result:
			result = diff
			if result == 0:
				print(0)
				sys.exit(0)
		return
	for i in range(depth, n + 1):
		entry.append(i)
		divide_team(i + 1)
		if entry.pop() == 1:
			return
divide_team(1)

print(result)
