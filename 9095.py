def road_to_n(now, goal):
	global cnt
	if now > goal:
		return
	if now == goal:
		cnt += 1
		return
	for i in range(1, 4):
		road_to_n(now + i, goal)

t = int(input())
for j in range(t):
	n = int(input())
	cnt = 0
	road_to_n(0, n)
	print(cnt)
