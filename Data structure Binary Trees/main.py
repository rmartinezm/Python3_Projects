from complete_binary_tree import CompleteBinaryTree

if __name__ == '__main__':

	tree = CompleteBinaryTree()
	
	for x in range(20):
		tree.add(x)

	for node in tree:
		print(node)

	print(tree.get_size())


