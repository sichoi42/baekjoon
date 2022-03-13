import sys
input=sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	coords = list(map(int, input().split()))
	sorted_coords = sorted(set(coords))
	rev_dict_coords = {i: v for v, i in enumerate(sorted_coords)}
	for x in coords:
		print(rev_dict_coords[x], end=' ')
