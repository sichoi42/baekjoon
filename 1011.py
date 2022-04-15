import sys, math

input = sys.stdin.readline

if __name__ == '__main__':
	for _ in range(int(input())):
		x, y = map(int, input().split())
		y = y - x
		x = 0
		crit = math.floor(y ** 0.5)
		surplus = math.ceil((y - crit ** 2) / crit)
		print(2 * crit - 1 + surplus)
