import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
max = float('-inf')
min = float('inf')

def calculate(result, idx):
	if idx == n - 1:
		global max, min
		if result > max:
			max = result
		if result < min:
			min = result
		return
	for i in range(4):
		if op[i] > 0:
			op[i] -= 1
			next = a[idx + 1]
			if i == 0:
				calculate(result + next, idx + 1)
			elif i == 1:
				calculate(result - next, idx + 1)
			elif i == 2:
				calculate(result * next, idx + 1)
			else:
				if result > 0:
					calculate(result // next, idx + 1)
				else:
					calculate(-((-result) // next), idx + 1)
			op[i] += 1
calculate(a[0], 0)

print(max)
print(min)
