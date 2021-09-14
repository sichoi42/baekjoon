from collections import deque, defaultdict

n, m = map(int, input().split(' '))
graph = defaultdict(list)
for _ in range(1, m + 1):
	v1, v2 = map(int, input().split(' '))
	graph[v1].append(v2)
	graph[v2].append(v1)

total_cnt = defaultdict(int)
for v in graph.keys():
	visited = defaultdict(bool)
	cnt = 1
	queue = deque([v])
	visited[v] = True
	while queue:
		qsize = len(queue)
		for _ in range(qsize):
			node = queue.popleft()
			for w in graph[node]:
				if visited[w] == False:
					visited[w] = True
					queue.append(w)
					total_cnt[v] += cnt
		cnt += 1
print(min(zip(total_cnt.values(), total_cnt.keys()))[1])
