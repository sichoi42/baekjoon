import sys

def main():
	s = set()
	m = int(input())
	for _ in range(m):
		op = sys.stdin.readline().rstrip().split()
		if len(op) == 2:
			x = int(op[1])
		op = op[0]
		if op == 'add':
			s.add(x)
		elif op == 'remove':
			try:
				s.remove(x)
			except:
				pass
		elif op == 'check':
			print(int(s.issuperset([x])))
		elif op == 'toggle':
			if s.issuperset([x]):
				s.remove(x)
			else:
				s.add(x)
		elif op == 'all':
			s = set([i for i in range(1, 21)])
		elif op == 'empty':
			s = set()

if __name__ == '__main__':
	main()
