# import sys

# def get_small(a, b):
# 	abs_a = abs(a)
# 	abs_b = abs(b)
# 	if abs_a < abs_b or (abs_a == abs_b and a < b):
# 		return a
# 	return b

# def insert(heap, x):
# 	heap.append(x)
# 	c = len(heap) - 1
# 	while c != 1:
# 		if get_small(heap[c], heap[c // 2]) == heap[c]:
# 			heap[c], heap[c // 2] = heap[c // 2], heap[c]
# 		else:
# 			break
# 		c //= 2

# def pop(heap):
# 	size = len(heap) - 1
# 	if size > 0:
# 		heap[size], heap[1] = heap[1], heap[size]
# 		result = heap.pop()
# 		size -= 1
# 		p = 1
# 		while p * 2 <= size:
# 			c = p * 2
# 			if c + 1 <= size and get_small(heap[c + 1], heap[c]) == heap[c + 1]:
# 				c += 1
# 			if get_small(heap[c], heap[p]) == heap[c]:
# 				heap[p], heap[c] = heap[c], heap[p]
# 			p = c
# 		return result
# 	return 0

# def main():
# 	heap = [None]
# 	n = int(input())
# 	for _ in range(n):
# 		x = int(sys.stdin.readline())
# 		if x != 0:
# 			insert(heap, x)
# 		else:
# 			print(pop(heap))

# if __name__ == '__main__':
	# main()

## using heapq

import sys
import heapq

def main():
	n = int(input())
	heap = []
	for _ in range(n):
		x = int(sys.stdin.readline())
		if x != 0:
			heapq.heappush(heap, (abs(x), x))
		else:
			if heap:
				print(heapq.heappop(heap)[1])
			else:
				print(0)

if __name__ == '__main__':
	main()
