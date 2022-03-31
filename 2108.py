import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	nums = [int(input())for _ in range(n)]
	print(round(sum(nums) / n))
	sorted_nums = sorted(nums)
	print(sorted_nums[n // 2])
	freq = defaultdict(int)
	for i in sorted_nums:
		freq[i] += 1
	max_freq = max(freq.values())
	candi = [k for k, v in freq.items() if v == max_freq]
	try:
		print(candi[1])
	except:
		print(candi[0])
	print(sorted_nums[n - 1] - sorted_nums[0])
