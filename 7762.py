import sys
import heapq
from collections import defaultdict

t = int(input())
for _ in range(t):
	k = int(input())

	min_heap = []
	max_heap = []
	atome = defaultdict(int)

	cnt = 0
	for __ in range(k):
		com, val = sys.stdin.readline().rstrip().split(' ')
		val = int(val)
		if com == "I":
			heapq.heappush(min_heap, val)
			heapq.heappush(max_heap, (-val, val))
			atome[val] += 1
			cnt += 1
		elif com == "D" and cnt > 0:
			if val == -1:
				poped = heapq.heappop(min_heap)
				while atome[poped] == 0:
					poped = heapq.heappop(min_heap)
			elif val == 1:
				poped = heapq.heappop(max_heap)[1]
				while atome[poped] == 0:
					poped = heapq.heappop(max_heap)[1]
			atome[poped] -= 1
			cnt -= 1
	if cnt == 0:
		print("EMPTY")
	else:
		min_poped = heapq.heappop(min_heap)
		while atome[min_poped] == 0:
			min_poped = heapq.heappop(min_heap)
		max_poped = heapq.heappop(max_heap)[1]
		while atome[max_poped] == 0:
			max_poped = heapq.heappop(max_heap)[1]
		print(max_poped, min_poped)
