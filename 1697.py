from collections import deque, defaultdict

n, k = map(int, input().split(' '))
queue = deque([n])
visited = defaultdict(bool)
cnt = 0
while queue:
	qsize = len(queue)
	for _ in range(qsize):
		cur = queue.popleft()
		if visited[cur] == False and 0 <= cur <= 100000:
			visited[cur] = True
			queue.append(cur - 1)
			queue.append(cur + 1)
			queue.append(cur * 2)
			if cur == k:
				print(cnt)
				exit(0)
	cnt += 1
