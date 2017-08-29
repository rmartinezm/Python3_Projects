from complete_binary_tree import CompleteBinaryTree
from binary_tree import BinaryTree

if __name__ == '__main__':

	tree = CompleteBinaryTree()
	
	for n in range(30):
		tree.add(n)

	print("Before to delete")
	for node in tree:
		print(node)
	print(tree.get_size())

	for n in range(29):
		tree.delete(n)

	print("After delete")
	for node in tree:
		print(node)
	print(tree.get_size())

	tree.delete(29)
	print("After delete all")
	for node in tree:
		print(node)
	print(tree.get_size())


	

