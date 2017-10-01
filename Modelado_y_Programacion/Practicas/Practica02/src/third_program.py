'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practicas/Practica02/src/third_program.py

	Escribe una función que se llame ropero tal que reciba como parámetros 3
	listas; una de camisetas, otra de pantalones y una de zapatos, la función
	debera regresar todas las combinaciones de atuendos posibles; ejemplo:
	ropero({’roja’, ’blanca’}, {’azul’, ’negro’, ’blanco’}, {’café, rojo’}) deberá re-
	gresar:
		Camiseta roja, pantalón azul y zapatos café
		Camiseta roja, pantalón azul y zapatos rojo
		Camiseta roja, pantalón negro y zapatos café
		...
'''

from itertools import product

'''
	Regresa todas las combinaciones posibles de atuendos con las tres listas que se reciben como parametro
	@param tshirts
		Lista de playeras
	@param pants
		Lista de pantalones
	@param shoes
		Lista de zapatos
	@return
		Una lista con las combinaciones de atuendos posibles
'''
def ropero(tshirts, pants, shoes):
	combinations = list(product(tshirts, pants, shoes))
	sList = []

	for combination in combinations:
		aCombination = "Camiseta {}, pantalón {} y zapatos {}".format(combination[0], combination[1], combination[2])
		sList.append(aCombination)

	return sList


if __name__ == '__main__':
	tshirts = ["roja", "blanca"]
	pants = ["azul", "negro", "blanco"]
	shoes = ["café", "rojo"]

	print("Camisetas:")
	print(tshirts)
	print("Pantalones:")
	print(pants)
	print("Zapatos:")
	print(shoes)
	print("\nLLamamos a la función ropero con estas listas\n")

	sList = ropero(tshirts, pants, shoes)
	for i in sList:
		print(i)
