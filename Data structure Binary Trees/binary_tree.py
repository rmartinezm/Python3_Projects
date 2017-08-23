import abc

class Node(object):

	'''
		Metodo constructor que recibe el elemento que guardara nuestro Nodo
	'''
	def __init__(self, element):
		self.element = element
		self.parent = None
		self.left_child = None
		self.right_child = None

	'''
		@return 
			El elemento que contiene nuestro nodo
	'''
	def get_element(self):
		return self.element

	'''
		@param element
			Elemento que queremos almacenar en nuestro nodo
	'''
	def set_element(self, elemet):
		self.elemet = elemet

	'''
		@return 
			El padre de nuestro nodo
	'''
	def get_parent(self):
		return self.parent

	'''
		@param node
			Nodo que asignaremos como padre
	'''
	def set_parent(self, node):
		self.parent = node

	'''
		@return 
			El hijo izquierdo de nuestro nodo
	'''
	def get_left_child(self):
		return self.left_child

	'''
		@param node
			Nodo que asignaremos como hijo izquierdo
	'''
	def set_left_child(self, node):
		self.left_child = node
		node.parent = self

	'''
		@return
			El hijo derecho de nuestro nodo
	'''
	def get_right_child(self):
		return self.right_child

	'''
		@param node
			Nodo que asignaremos como hijo derecho
	'''
	def set_right_child(self, node):
		self.right_child = node
		node.parent = self

	'''
		@return 
			True si el hijo izquierdo es distinto de None
			False en otro caso
	'''
	def have_left_child(self):
		return self.left_child != None

	'''
		@return 
			True si el hijo derecho es distinto de None
			False en otro caso
	'''
	def have_right_child(self):
		return self.right_child != None

	'''
		@return
			Representacion en forma de cadena de nuestro nodo
	'''
	def __str__(self):
		return "( " + str(self.element) + " )"



class BinaryTree(object):

	__metaclass__ = abc.ABCMeta

	'''
		Metodo constructor que inicializa el arbol con la raiz None 
		y el tamanio en 0
	'''
	def __init__(self):
		self.root = None
		self.size = 0

	'''
		Metodo abstracto que nos indicara como agregar elementos al arbol
	'''
	@abc.abstractmethod
	def add(self, element):
		'''
		Metodo que nos indicara como agregar un elemento al arbol
		'''
		raise BaseException("Method not implemented")

	'''
		Metodo que nos indica como eliminaremos a un elemento del arbol
	'''
	@abc.abstractmethod
	def delete(self, element):		
		'''
			Metodo que nos indica como eliminaremos a un elemento del arbol
		'''
		raise BaseException("Method not implemented")

	'''
		Metodo que creara un tipo especifico de nodo dependiendo de lo que necesite
		el arbol
	'''
	def new_node(self, element):
		return Node(element)

	'''
		@return
			El tamanio de nuestro arbol
	'''
	def get_size(self):
		return self.size

	'''
		@return
			True si el arbol esta vacio
			False en otro caso
	'''
	def is_empty(self):
		return self.size == 0

