from arbol_binario_completo import ArbolBinarioCompleto

if __name__ == '__main__':

	arbol = ArbolBinarioCompleto()
	arbol.agrega("Hola")
	arbol.agrega("Mundo")
	arbol.agrega("Desde")
	arbol.agrega("Python3")

	for nodo in arbol:
		print(nodo)
	for nodo in arbol:
		print(nodo)
