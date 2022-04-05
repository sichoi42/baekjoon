from collections import deque, defaultdict

n, k = map(int, input().split(' '))
queue = deque([n])
visited = defaultdict(lambda: -1)
visited[n] = 0
while queue:
	cur = queue.popleft()
	if cur == k:
		print(visited[cur])
		break
	if 0 <= cur <= 100000:
		nexts = [cur - 1, cur + 1, cur * 2]
		for next in nexts:
			if visited[next] == -1:
				queue.append(next)
				visited[next] = visited[cur] + 1
