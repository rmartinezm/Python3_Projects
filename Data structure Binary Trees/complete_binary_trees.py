from arbol_binario import ArbolBinario
from arbol_binario import Nodo 

class ArbolBinarioCompleto(ArbolBinario):

	def __init__(self):
		super(ArbolBinarioCompleto, self).__init__()
		self.cola_para_iterar = []

	def agrega(self, elemento):
		nodo = self.nuevo_nodo(elemento)
		if (self.estoy_vacio()):
			self.raiz = nodo
		else:
			lista = [self.raiz]
			self.agrega_recursivo(lista, nodo)
		self.tamanio += 1

	def agrega_recursivo(self, lista, nodo):
		nodo_aux = lista.pop(0)
		if (not nodo_aux.tengo_hijo_izq()):
			nodo_aux.set_hijo_izq(nodo)
		elif (not nodo_aux.tengo_hijo_der()):
			nodo_aux.set_hijo_der(nodo)
		else:
			lista.append(nodo_aux.get_hijo_izq())
			lista.append(nodo_aux.get_hijo_der())
			self.agrega_recursivo(lista, nodo)

	def elimina(self, elemento):
		pass

	def __iter__(self):
		if (self.raiz != None):
			self.cola_para_iterar.append(self.raiz)
		return self

	def __next__(self):
		if not self.cola_para_iterar:
			raise StopIteration
		nodo = self.cola_para_iterar.pop(0)
		if (nodo.tengo_hijo_izq()):
			self.cola_para_iterar.append(nodo.get_hijo_izq())
		if (nodo.tengo_hijo_der()):
			self.cola_para_iterar.append(nodo.get_hijo_der())
		return nodo


