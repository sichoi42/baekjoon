import sys

input = sys.stdin.readline

class Node:
	def __init__(self, data, left, right) -> None:
		self.data = data
		self.left = left
		self.right = right

def preorder(node):
	print(node.data, end='')
	if node.left != '.' and node.left != None:
		preorder(tree[node.left])
	if node.right != '.' and node.right != None:
		preorder(tree[node.right])

def inorder(node):
	if node.left != '.' and node.left != None:
		inorder(tree[node.left])
	print(node.data, end='')
	if node.right != '.' and node.right != None:
		inorder(tree[node.right])

def postorder(node):
	if node.left != '.' and node.left != None:
		postorder(tree[node.left])
	if node.right != '.' and node.right != None:
		postorder(tree[node.right])
	print(node.data, end='')

if __name__ == '__main__':
	tree = {}
	n = int(input())
	for _ in range(n):
		node, left, right = input().rstrip().split()
		tree[node] = Node(node, left, right)
	preorder(tree['A'])
	print()
	inorder(tree['A'])
	print()
	postorder(tree['A'])
	print()
