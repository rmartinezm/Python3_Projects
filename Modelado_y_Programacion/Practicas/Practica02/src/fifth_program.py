'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica02/src/fifth_program.py

	Escribe una función que implemente el algoritmo de búsqueda binaria

	La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada de elementos.
	Funciona al dividir repetidamente a la mitad la porción de la lista que podría contener al elemento,
	hasta reducir las ubicaciones posibles a solo una.
'''

from random import randrange

'''
	Regresa el índice de un elemento dentro de la lista utilizando el algoritmo de busqueda binaria
	@param element
		El elemento que buscamos
	@return 
		El índice del elemento dentro de la lista si este está en la lista
		None en otro caso
'''
def binary_search(aList, element):
	L, R = 0, len(aList)
	while R >= L:
		i = int(L + ((R - L) / 2))
		if (aList[i] == element):
			return i
		else:
			if (aList[i] < element):
				L = i + 1
			else:
				R = i - 1
	return None


if __name__ == '__main__':
	aList = []
	for i in range(30):
		aList.append(randrange(100))
	to_search = aList[0]
	aList.sort()

	print("Lista ordenada: ")
	print(aList)
	print("Elemento del que queremos el indice: " + str(to_search))
	print("Índice dónde se encuentra el elemento: " + str(binary_search(aList, to_search)))



