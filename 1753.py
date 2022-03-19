import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
	V, E = map(int, input().split())
	K = int(input())
	adj = [[] for _ in range(V + 1)]
	for _ in range(E):
		u, v, w = map(int, input().split())
		adj[u].append((w, v))
	dist = [float('INF') for _ in range(V + 1)]
	dist[K] = 0
	queue = []
	heapq.heappush(queue, (0, K))
	while queue:
		cost, node = heapq.heappop(queue)
		if dist[node] < cost:
			continue
		for w, v in adj[node]:
			if dist[v] > dist[node] + w:
				dist[v] = dist[node] + w
				heapq.heappush(queue, (dist[v], v))
	for i in range(1, V + 1):
		result = dist[i]
		if result == float('inf'):
			print("INF")
		else:
			print(result)
