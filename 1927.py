import sys

def del_min(heap):
	size = len(heap) - 1
	if size > 0:
		heap[size], heap[1] = heap[1], heap[size]
		result = heap.pop()
		size -= 1
		p = 1
		while p * 2 <= size:
			c = p * 2
			if c + 1 <= size and heap[c] > heap[c + 1]:
				c += 1
			if heap[p] > heap[c]:
				heap[p], heap[c] = heap[c], heap[p]
			p = c
		return result
	return 0

def insert_min(heap, data):
	heap.append(data)
	size = len(heap) - 1
	c = size
	while c != 1:
		if heap[c] < heap[c // 2]:
			heap[c], heap[c // 2] = heap[c // 2], heap[c]
		c //= 2

def main():
	n = int(input())
	heap = [-1]
	for _ in range(n):
		cal = int(sys.stdin.readline())
		if cal == 0:
			print(del_min(heap))
		else:
			insert_min(heap, cal)


if __name__ == '__main__':
	main()