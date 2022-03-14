import sys

input = sys.stdin.readline

if __name__ == '__main__':
	n, m = map(int, input().split())
	site_dict = {site: pwd for site, pwd in [input().rstrip().split() for _ in range(n)]}
	for _ in range(m):
		print(site_dict[input().rstrip()])
