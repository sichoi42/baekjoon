import sys
import heapq

input = sys.stdin.readline

def short_cut(adj, dist):
	queue = []
	heapq.heappush(queue, (0, x))
	while queue:
		cost, node = heapq.heappop(queue)
		if dist[node] < cost:
			continue
		for v, w in adj[node].items():
			prev = dist[node] + w
			if dist[v] > prev:
				dist[v] = prev
				heapq.heappush(queue, (dist[v], v))

n, m, x = map(int, input().split())
adj = {i: dict() for i in range(1, n + 1)}
adj_rev = {i: dict() for i in range(1, n + 1)}
for _ in range(m):
	a, b, c = map(int, input().split())
	adj[a][b] = c
	adj_rev[b][a] = c

dist = {i: float('inf') for i in range(1, n + 1)}
dist_rev = {i: float('inf') for i in range(1, n + 1)}
dist[x] = dist_rev[x] = 0

short_cut(adj, dist)
short_cut(adj_rev, dist_rev)
result = 0
for i in range(1, n + 1):
	result = max(result, dist[i] + dist_rev[i])
print(result)
