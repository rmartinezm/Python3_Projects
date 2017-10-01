"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practicas/Practica03/src/second_program.py

	Crea la clase llamada Fruta, una fruta debe tener tamaño (grande, mediana, pequeña) y color.

	Crea las clases Fresa, Mango, Sandı́a y Toronja que extiendan a Fruta; estas clases deben agregar las propiedades:
	sabor (dulce, ácido o amargo) y la propiedad conCascara que será una variable
	booleana que valdrá true, en caso de que la fruta posea una cáscara no comestible, como el caso de
	la sandı́a en nuestra lista de frutas.
	Deberás crear una lista genérica por cada fruta con sabores, colores y tamaños al azar. Cada lista
	de frutas se puede llamar canasta.
	Tendrás que implementar métodos que permitan realizar las siguientes operaciones:
	contiene(self, fruta)
	Este método regresa true cuando una fruta está dentro de una canasta
	tamanio(self)
	Este método regresa la cantidad de frutas contenidas en una canasta
	revuelve(self)
	Este método regresa una canasta de longitud mayor que contendrá frutas de dos tipos distintos
	limpia(self)
	Este método recibe una canasta de frutas que pueden ser de tamaños y sabores distintos, pero
	sólo se queda con las frutas que son de sabor dulce y tamaño grande elimando las que no lo
	son.
	cuenta(self)
	Este método recibe una canasta de frutas e imprimirá en pantalla la cantidad de frutas de
	color distinto que haya, ejemplo: 3 rojas, 1 amarilla
"""

from first_program import InvalidParametersException
from itertools import chain
from random import randrange

class Fruta(object):

	def __init__(self, tamanio, color):
		if (tamanio == "Grande" or tamanio == "Mediana" or tamanio == "Pequeña"):
			self.tamanio = tamanio
		else:
			raise InvalidParametersException()
		self.color = color

class Fresa(Fruta):

	def __init__(self, tamanio, color, sabor, conCascara):
		super(Fresa, self).__init__(tamanio, color)
		if (sabor == "Dulce" or sabor == "Ácido" or sabor == "Amargo"):
			self.sabor = sabor
		else:
			raise InvalidParametersException()
		self.conCascara = conCascara

	def __str__(self):
		return "Fresa {} de color {} con sabor {} y su cascara {}".format(self.tamanio, self.color, self.sabor, "no es comestible" if self.conCascara else "es comestible")


class Mango(Fruta):

	def __init__(self, tamanio, color, sabor, conCascara):
		super(Mango, self).__init__(tamanio, color)
		if (sabor == "Dulce" or sabor == "Ácido" or sabor == "Amargo"):
			self.sabor = sabor
		else:
			raise InvalidParametersException()
		self.conCascara = conCascara

	def __str__(self):
		return "Mango {} de color {} con sabor {} y su cascara {}".format(self.tamanio, self.color, self.sabor, "no es comestible" if self.conCascara else "es comestible")



class Sandia(Fruta):

	def __init__(self, tamanio, color, sabor, conCascara):
		super(Sandia, self).__init__(tamanio, color)
		if (sabor == "Dulce" or sabor == "Ácido" or sabor == "Amargo"):
			self.sabor = sabor
		else:
			raise InvalidParametersException()
		self.conCascara = conCascara

	def __str__(self):
		return "Sandía {} de color {} con sabor {} y su cascara {}".format(self.tamanio, self.color, self.sabor, "no es comestible" if self.conCascara else "es comestible")



class Toronja(Fruta):

	def __init__(self, tamanio, color, sabor, conCascara):
		super(Toronja, self).__init__(tamanio, color)
		if (sabor == "Dulce" or sabor == "Ácido" or sabor == "Amargo"):
			self.sabor = sabor
		else:
			raise InvalidParametersException()
		self.conCascara = conCascara

	def __str__(self):
		return "Toronja {} de color {} con sabor {} y su cascara {}".format(self.tamanio, self.color, self.sabor, "no es comestible" if self.conCascara else "es comestible")


class Canasta(object):

	def __init__(self, canasta):
		self.canasta = canasta

	def contiene(self, fruta):
		return fruta in self.canasta

	def tamanio(self):
		return len(self.canasta)

	def revuelve(self, other):
		aList = list(chain(self.canasta, other))
		return Canasta(aList)

	def limpia(self):
		nueva_lista = []
		for fruta in self.canasta:
			if (fruta.tamanio == "Grande" and fruta.sabor == "Dulce"):
				nueva_lista.append(fruta)
		self.canasta = nueva_lista

	def cuenta(self):
		aDictionary = {}
		for fruta in self.canasta:
			if fruta.color in aDictionary:
				valor = aDictionary.get(fruta.color)
				valor += 1
				aDictionary[fruta.color] = valor
			else:
				aDictionary[fruta.color] = 1
		
		aString = ""
		for key in aDictionary.keys():
			aString += "{} {}, ".format(aDictionary[key], key)
		if aString != "":
			aString = aString[:len(aString)-2]
		print(aString)

if __name__ == '__main__':
 	
 	# Valores que tomaremos al azar
 	tamanios = ["Grande", "Mediana", "Pequeña"]
 	colores = ["Rojo", "Amarillo", "Verde", "Azul", "Morado", "Gris", "Negro", "Blanco"] 
 	sabores = ["Dulce", "Ácido", "Amargo"]

 	# Inicialización de las canastas de fruta
 	canastaFresas = []
 	for i in range(5):
 		canastaFresas.append(Fresa(tamanios[randrange(3)], colores[randrange(8)], sabores[randrange(3)], False))
 	canastaFresas = Canasta(canastaFresas)

 	canastaMangos = []
 	for i in range(5):
 		canastaMangos.append(Mango(tamanios[randrange(3)], colores[randrange(8)], sabores[randrange(3)], True))
 	canastaMangos = Canasta(canastaMangos)

 	# Para ejemplificar los métodos solo se usará la canasta de Fresas
 	unaFresa = canastaFresas.canasta[0]
 	print("\nUna fruta que sí está en la canasta el método contiene regresa: ")
 	print(canastaFresas.contiene(unaFresa))
 	# Con el parametro conCascara igual a True aseguramos que no estará en ninguna combinacion posible en canastaFresas
 	unaFresa = Fresa("Grande", "Rojo", "Dulce", True)
 	print("Una fruta que no está en la canasta el método contiene regresa: ")
 	print(canastaFresas.contiene(unaFresa))

 	# Tamanio de la canasta de Fresas
 	print("\nEl tamaño de la canasta de fresas es: " + str(canastaFresas.tamanio()))

 	# Revuelve canastaFresas con canastaMangos
 	print("\nRevolvemos una canasta de fresas con una de mangos")
 	canastaFresasMangos = canastaFresas.revuelve(canastaMangos.canasta)
 	print("El tamaño de la nueva lista es: " + str(canastaFresasMangos.tamanio()))

 	# Contamos las frutas con los colores
 	print("\nAplicando el método cuenta tenemos: ")
 	canastaFresasMangos.cuenta()

 	# Limpiamos la canasta nueva
 	print("\nAplicamos el método limpa y tenemos: ")
 	canastaFresasMangos.limpia()
 	if (canastaFresasMangos.canasta == []):
 		print("No hay frutas con las caracteristicas de ser Dulces y Grandes")
 	else:
 		for fruta in canastaFresasMangos.canasta:
 			print(fruta)