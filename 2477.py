import sys
from collections import deque, defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
	k = int(input())
	vector = defaultdict(int)
	queue = deque()
	for _ in range(6):
		v, l = map(int, input().split())
		vector[v] += 1
		queue.append((v, l))
	result = 0
	if vector[1] == 2: # 동이 2개
		while queue[0][0] != 2: # 서쪽 반향이 맨 앞으로
			queue.append(queue.popleft())
		if vector[3] == 2: # ㄱ 모양
			result = queue[0][1] * queue[5][1] - queue[2][1] * queue[3][1]
		else:
			result = queue[0][1] * queue[1][1] - queue[3][1] * queue[4][1]
	else:
		if vector[4] == 2: # ㄴ 모양
			while queue[0][0] != 3: # 남쪽 반향이 맨 앞으로
				queue.append(queue.popleft())
		else:
			while queue[0][0] != 1: # 동쪽 반향이 맨 앞으로
				queue.append(queue.popleft())
		result = queue[0][1] * queue[1][1] - queue[3][1] * queue[4][1]
	print(k * result)
