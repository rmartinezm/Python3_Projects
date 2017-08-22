from binary_tree import BinaryTree
# from binary_tree import Node 

class CompleteBinaryTree(BinaryTree):

	'''
		Metodo constructor que asigna una lista para poder iterar el arbol
	'''
	def __init__(self):
		super(CompleteBinaryTree, self).__init__()
		self.list_to_iterable = []

	
	'''
		Metodo que nos indica como agregar un elemento al arbol
	'''
	def add(self, element):
		node = self.new_node(element)
		if (self.is_empty()):
			self.root = node
		else:
			list_aux = [self.root]
			self.__add(list_aux, node)
		self.size += 1

	'''
		Metodo auxiliar para agregar un elemento al arbol
	'''
	def __add(self, list_aux, node):
		node_aux = list_aux.pop(0)
		if (not node_aux.have_left_child()):
			node_aux.set_left_child(node)
		elif (not node_aux.have_right_child()):
			node_aux.set_right_child(node)
		else:
			list_aux.append(node_aux.get_left_child())
			list_aux.append(node_aux.get_right_child())
			self.__add(list_aux, node)

	'''
		Metodo que nos indica como eliminar un elemento al arbol
	'''
	def delete(self, element):
		return

	'''
		@return
			Un iterable del arbol 
	'''
	def __iter__(self):
		if (self.root != None):
			self.list_to_iterable.append(self.root)
		return self

	'''
		@return 
			El siguiente elemento del iterable
	'''
	def __next__(self):
		if not self.list_to_iterable:
			raise StopIteration
		node = self.list_to_iterable.pop(0)
		if (node.have_left_child()):
			self.list_to_iterable.append(node.get_left_child())
		if (node.have_right_child()):
			self.list_to_iterable.append(node.get_right_child())
		return node


