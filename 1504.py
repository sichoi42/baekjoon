import sys
import heapq

input = sys.stdin.readline

def short_len(a, b):
	queue = []
	heapq.heappush(queue, (0, a))
	dist = [float('inf') for _ in range(n + 1)]
	dist[a] = 0
	while queue:
		cost, node = heapq.heappop(queue)
		if dist[node] < cost:
			continue
		for w, v in adj[node]:
			if dist[v] > dist[node] + w:
				dist[v] = dist[node] + w
				heapq.heappush(queue, (dist[v], v))
	return dist[b]

def road_to_n(fst, sec, n):
	result = 0
	result += short_len(1, fst)
	if result == float('inf'):
		return -1
	result += short_len(fst, sec)
	if result == float('inf'):
		return -1
	result += short_len(sec, n)
	if result == float('inf') or result == 0:
		return -1
	return result

def get_min(a, b):
	if a == -1 and b == -1:
		return -1
	elif a == -1:
		return b
	elif b == -1:
		return a
	else:
		return min(a, b)

if __name__ == '__main__':
	n, m = map(int, input().split())
	adj = [[] for _ in range(n + 1)]
	for _ in range(m):
		a, b, c = map(int, input().split())
		adj[a].append((c, b))
		adj[b].append((c, a))
	v1, v2 = map(int, input().split())
	print(get_min(road_to_n(v1, v2, n), road_to_n(v2, v1, n)))
