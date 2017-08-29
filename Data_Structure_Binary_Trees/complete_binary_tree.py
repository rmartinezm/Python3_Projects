from binary_tree import *

"""
	@author
		Roberto Martínez Medina
	@github
		https://github.com/rmartinezm/Python3_Projects/blob/master/Data%20structure%20Binary%20Trees/complete_binary_tree.py
"""

'''
	Arbol Binario Completo
    Un árbol binario completo es un árbol binario de profundidad K que tiene todos los nodos posibles hasta
    el penúltimo nivel (profundidad K-1), y donde los elementos del último nivel están colocados de izquierda
    a derecha sin dejar huecos entre ellos.
'''
class CompleteBinaryTree(BinaryTree):

	'''
		Metodo constructor que asigna una lista para poder iterar el arbol
	'''
	def __init__(self):
		super(CompleteBinaryTree, self).__init__()
		self.list_to_iterable = []

	
	'''
		Metodo que agrega un elemento al arbol
		@param element
			El elemento que agregaremos al arbol
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
		Metodo privado auxiliar para agregar un elemento al arbol
		@param list_aux 
			Lista que utilizaremos para iterar el arbol y poder agregar
			el nodo deseado
		@param node
			El nodo que agregaremos al arbol
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
		Metodo que elimina un elemento del arbol
		@param element
			El elemento que eliminaremos del arbol
		@raise ElementNotFound
			Si el elemento no se encuentra en el arbol
		@raise MethodNotImplement
			Si el metodo aun no ha sido implementado
	'''
	def delete(self, element):
		node_element = self.__search(element)
		if (node_element == None):
			raise ElementNotFound()

		last_node = self.__get_last_node()

		node_element.set_element(last_node.get_element())

		self.__delete_last_node()
		self.size -= 1

	'''
		Metodo privado auxiliar que es utilizado para buscar un nodo en el arbol
		@return 
			El nodo si esta en el arbol
			None en otro caso
	'''
	def __search(self, element):
		for node in self:
			if (node.get_element() == element):
				self.list_to_iterable = []
				return node
		return None


	'''
		Metodo privado auxiliar que es utilizado para eliminar el ultimo nodo del arbol
	'''
	def __delete_last_node(self):
		node = self.__get_last_node()
		if (node.get_parent() == None):
			self.clear()
		else:
			if (node.im_left_child()):
				node.get_parent().set_left_child(None)
			else:
				node.get_parent().set_right_child(None)

	'''
		Metodo privado auxiliar que es utilizado para devolver el ultimo nodo del arbol
		@return
			El ultimo nodo del arbol 
	'''
	def __get_last_node(self):
		n = 0
		if (self.size == 0):
			return None
		for node in self:
			n += 1
			if (n == self.size):
				return node


	'''
		Metodo que regresa un iterable del arbol
		@return
			Un iterable del arbol 
	'''
	def __iter__(self):
		if (self.root != None):
			self.list_to_iterable.append(self.root)
		return self

	'''
		Elemento que nos regresa el siguiente elemento de iteracion
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


