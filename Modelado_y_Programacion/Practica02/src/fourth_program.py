'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica02/fourth_program.py

	Escribe un función que reciba dos arreglos ordenados A1 y A2 y regrese
	un arreglo B que contenga todos los elementos de A1 y A2 y que también
	esté ordenado
'''

from itertools import chain
from random import randrange

'''
	Regresa una lista ordenada con todos los elementos de las listas que se 
	pasan como parametros
	@param plist_one
		Lista ordenada numero uno
	@param plist_two
		Lista ordenada numero dos
	@return
		Una lista ordenada con los elementos de plist_one y plist_two 
'''
def merge(plist_one, plist_two):
	list_one, list_two = plist_one[:], plist_two[:]
	merge_list = []
	
	while list_one != [] and list_two != []:
		if (list_one[0] <= list_two[0]):
			merge_list.append(list_one.pop(0))
		else:
			merge_list.append(list_two.pop(0))

	return list(chain(merge_list, list_one, list_two))


'''
	Regresa una lista ordenada con todos los elementos de las listas que se 
	pasan como parametros
	@param plist_one
		Lista no necesariamente ordenada numero uno
	@param plist_two
		Lista no necesariamente ordenada numero dos
	@return
		Una lista ordenada con los elementos de plist_one y plist_two 
'''
def easy_merge(plist_one, plist_two):
	return sorted(list(chain(plist_one, plist_two)))

if __name__ == '__main__':
	plist_one = []
	for i in range(10):
		plist_one.append(randrange(100))
	plist_one.sort()
	print("A1:")
	print(plist_one)

	plist_two = []
	for i in range(10):
		plist_two.append(randrange(100))
	plist_two.sort()
	print("A2:")
	print(plist_two)

	listB = merge(plist_one, plist_two)  # Mismo resultado si usamos easy_merge(plist_one, plist_two)
	print("B:")
	print(listB)


