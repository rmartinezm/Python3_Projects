'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practicas/Practica02/src/second_program.py

	Implementar el algoritmo de ordenamiento Insertion Sort

	Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
	It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
	However, insertion sort provides several advantages:
    
    	* Simple implementation: Jon Bentley shows a three-line C version, and a five-line optimized version.
    	* Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    	* More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
    	* In-place; i.e., only requires a constant amount O(1) of additional memory space

	Fuente: https://en.wikipedia.org/wiki/Insertion_sort
'''

from random import randrange

'''
	Ordena una lista utilizando el algoritmo Insertion Sort (El algoritmo se aplica in-place)
	@param aList
		La lista que queremos ordenar
'''
def insertion_sort(aList):
	for i in range(1, len(aList)):
		j = i
		while j > 0 and aList[j] < aList[j-1]:
			aList[j], aList[j-1] = aList[j-1], aList[j]
			j -= 1


if __name__ == '__main__':
	i = 0
	myList = []	
	while (i < 20):
		myList.append(randrange(100))
		i += 1
	print("Before insertion_sort:")
	print(myList)
	insertion_sort(myList)
	print("After insertion_sort:")
	print(myList)