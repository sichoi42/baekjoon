import sys

def insert_heap(heap, data):
	heap.append(data)
	size = len(heap) - 1
	c = size
	while c != 1:
		if heap[c] > heap[c // 2]:
			heap[c], heap[c // 2] = heap[c // 2], heap[c]
		c //= 2

def del_max(heap):
	size = len(heap) - 1
	if size > 0:
		heap[1], heap[size] = heap[size], heap[1]
		result = heap.pop()
		size -= 1
		p = 1
		while 2 * p <= size:
			c = 2 * p
			if c + 1 <= size and heap[c + 1] > heap[c]:
				c += 1
			if heap[c] > heap[p]:
				heap[p], heap[c] = heap[c], heap[p]
			else:
				break
			p = c
		return result
	return 0

def main():
	n = int(input())
	heap = [-1]
	for _ in range(n):
		cal = int(sys.stdin.readline())
		if cal == 0:
			print(del_max(heap))
		else:
			insert_heap(heap, cal)

if __name__ == '__main__':
	main()