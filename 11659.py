import sys

input = sys.stdin.readline

def main():
	n, m = list(map(int, input().rstrip().split()))
	arr = list(map(int, input().rstrip().split()))
	sums = [0, arr[0]]
	for i in range(2, n + 1):
		sums.append(sums[i - 1] + arr[i - 1])
	for _ in range(m):
		i, j = list(map(int, input().rstrip().split()))
		print(sums[j] - sums[i - 1])

if __name__ == '__main__':
	main()
