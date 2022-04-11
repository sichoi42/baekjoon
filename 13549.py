# import heapq
# import sys

# input = sys.stdin.readline

# if __name__ == '__main__':
# 	n, k = map(int, input().split())
# 	queue = []
# 	heapq.heappush(queue, (0, n))
# 	dist = {i: float('inf') for i in range(100001)}
# 	dist[n] = 0
# 	while queue:
# 		cost, node = heapq.heappop(queue)
# 		if dist[node] > cost:
# 			continue
# 		for w, v in [(1, node - 1), (1, node + 1), (0, node * 2)]:
# 			if 0 <= v <= 100000:
# 				next = dist[node] + w
# 				if next < dist[v]:
# 					dist[v] = next
# 					heapq.heappush(queue, (dist[v], v))
# 	print(dist[k])


import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
	n, k = map(int, input().split())
	queue = deque([n])
	dist = [float('inf')] * 100001
	dist[n] = 0
	while queue:
		cur = queue.popleft()
		if cur == k:
			print(dist[k])
			break
		next = cur - 1
		if next >= 0 and dist[next] > dist[cur] + 1:
			dist[next] = dist[cur] + 1
			queue.append(next)
		next = cur + 1
		if next <= 100000 and dist[next] > dist[cur] + 1:
			dist[next] = dist[cur] + 1
			queue.append(next)
		next = cur * 2
		if next <= 100000 and dist[next] > dist[cur]:
			dist[next] = dist[cur]
			queue.appendleft(next)
