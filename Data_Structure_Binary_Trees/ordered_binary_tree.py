from binary_tree import BinaryTree

# Arbol Binario Ordenado
'''
	Los elementos que quieran ser almacenados en un arbol binario ordenado deberan de extender de la clase
	Comparable del archivo comparable.py 
'''
class OrderedBinarTree(BinaryTree):

	def __init__(self):
		self.__init__(self)

	'''
		Metodo que agrega al arbol binario ordenado el elemento que nos pasan como parametro
		@param element 
			El elemento que agregaremos a nuestro arbol binario ordenado
	'''
	def add(self, element):
		node = self.new_node(element)
		if (self.root == None):
			self.root = node
		else:
			self.__add_aux(root, node)
		self.size += 1 

	'''
		Metodo privado que nos servira para agregar el nodo en su posicion dentro del arbol
		binario ordenado.
	'''		
	def __add_aux(self, node, node_to_add):
		if (node_to_add.compare_to(node) > 0):
			if (not node.has_right_child()):
				node.set_right_child(node_to_add)
			else:
				self.__add_aux(node.get_right_child(), node_to_add)
		else:
			if (not node.has_left_child()):
				node.set_left_child(node_to_add)
			else:
				self.__add_aux(node.get_left_child(), node_to_add)

	def elimina(self, elemento):
		pass

	def __iter__(self):
		return self

	def __next__(self):

		pass

	def __eq__(self, other):
		if (isinstance(other, self.__class__)):
			nodo_uno = self.raiz
			nodo_dos = other.raiz
			return self.son_iguales(nodo_uno, nodo_dos)
		return False

	def son_iguales(self, nodo_uno, nodo_dos):
		if (not nodo_uno == nodo_dos):
			return False
		return self.son_iguales(nodo_uno.get_hijo_izq(), nodo_dos.get_hijo_izq()) and self.son_iguales(nodo_uno.get_hijo_der(), nodo_dos.get_hijo_der())  

