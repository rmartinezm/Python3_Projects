import abc

'''
	Interface para objetos que necesiten poder ser comparados 
'''
class Comparable(object):

	__metaclass_= abc.ABCMeta

	@abc.abstractmethod
	def compare_to(self, other):
		'''
		El metodo debe de comparar nuestro objeto con el objeto 'other' 
		@param other
			un objeto con el que tenemos que comparar nuestro objeto 
		@return 
			un entero mayor que 0 si nuestro objeto es mayor que el objeto other.
			0 si nuestro objeto es igual que el objeto other.
			un numero menor que 0 si nuestro objeto es menor que el objeto other.
		'''
		return

