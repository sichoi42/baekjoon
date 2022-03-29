import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
	n, m = int(input()), int(input())
	adj = [[] for _ in range(n + 1)]
	for _ in range(m):
		a, b, c = map(int, input().split())
		adj[a].append((c, b))
	a, b = map(int, input().split())
	dist = [float('inf') for _ in range(n + 1)]
	dist[a] = 0
	queue = []
	heapq.heappush(queue, (0, a))
	while queue:
		cost, node = heapq.heappop(queue)
		if dist[node] < cost:
			continue
		for w, v in adj[node]:
			if dist[v] > dist[node] + w:
				dist[v] = dist[node] + w
				heapq.heappush(queue, (dist[v], v))
	print(dist[b])
