import abc

class Nodo(object):

	'''
	Metodo constructor que recibe el elemento que guardara nuestro Nodo
	'''
	def __init__(self, elemento):
		self.elemento = elemento
		self.padre = None
		self.hijo_izquierdo = None
		self.hijo_derecho = None

	def get_elemento(self):
		return self.elemento

	def get_padre(self):
		return self.padre

	def set_padre(self, nodo):
		self.padre = nodo

	def get_hijo_izq(self):
		return self.hijo_izquierdo

	def set_hijo_izq(self, nodo):
		self.hijo_izquierdo = nodo
		nodo.padre = self

	def get_hijo_der(self):
		return self.hijo_derecho

	def set_hijo_der(self, nodo):
		self.hijo_derecho = nodo
		nodo.padre = self

	def tengo_hijo_izq(self):
		return self.hijo_izquierdo != None

	def tengo_hijo_der(self):
		return self.hijo_derecho != None

	def __str__(self):
		return str(self.elemento)



class ArbolBinario(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self):
		self.raiz = None
		self.tamanio = 0

	@abc.abstractmethod
	def agrega(self, elemento):
		'''
		Metodo que nos indica como tenemos que agregar un elemento a nuestro
		arbol binario
		'''
		return 

	@abc.abstractmethod
	def elimina(self, elemento):
		'''
		Metodo que nos indica como tenemos que eliminar a un elemento a nuestro
		arbol binario
		'''
		return 

	def nuevo_nodo(self, elemento):
		return Nodo(elemento)

	def get_tamanio(self):
		return self.tamanio

	def estoy_vacio(self):
		return self.tamanio == 0



		