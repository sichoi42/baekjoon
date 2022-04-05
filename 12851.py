import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
	n, k = map(int, input().split())
	queue = deque([n])
	visited = [-1] * 100001
	cnt = [0] * 100001
	visited[n] = 0
	cnt[n] = 1
	while queue:
		cur = queue.popleft()
		for next in [cur - 1, cur + 1, cur * 2]:
			if 0 <= next <= 100000:
				if visited[next] == -1: # 방문한 적이 없는 경우
					visited[next] = visited[cur] + 1
					cnt[next] = cnt[cur]
					queue.append(next)
				elif visited[next] == visited[cur] + 1: # 다른 분기가 먼저 방문한 경우
					cnt[next] = cnt[next] + cnt[cur] # 다른 분기에서 발생한 경우의 수 + 현재 분기에서 발생한 경우의 수로 업데이트
	print(visited[k], cnt[k], sep='\n')
