from itertools import combinations
import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n, m = map(int, input().split())
	house = []
	chicken = []
	for i in range(n):
		lst = list(map(int, input().split()))
		for j in range(n):
			if lst[j] == 1:
				house.append((i, j))
			elif lst[j] == 2:
				chicken.append((i, j))
	cases = list(combinations(chicken, m))

	min = float('inf')
	for case in cases:
		sum = 0
		for h_r, h_c in house:
			dist_chick = float('inf')
			for c_r, c_c in case:
				dist = abs(h_r - c_r) + abs(h_c - c_c)
				if dist < dist_chick:
					dist_chick = dist
			sum += dist_chick
		if sum < min:
			min = sum
	print(min)

