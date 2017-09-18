"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica03/src/third_program.py

	Crea la clase Especie, de ella deberán heredar las clases Herbı́voro y Carnı́voro.

	Crea las clases:
	Leon y Tiburón que hereden de Carnı́voro y las clases Jirafa y Elefante que hereden de Herbı́voro,
	por otro lado crea la clase SerHumano y Planta. El SerHumano deberá heredar de Carnı́voro y Herbı́voro.

	Crea el método alimentarse() el cual para los carnı́voros al recibir como parámetro objetos de tipo
	Carnı́voro, Herbı́voro y SerHumano imprima en pantalla A comer!!!, en caso de recibir objetos
	de tipo Planta imprima Nooo... gracias.

	Para los objetos de tipo SerHumano este método deberá recibir y aceptar bien objetos de tipo
	Carnı́voro y Herbı́voro salvo otros Seres Humanos.

	Los hervı́voros sólo pueden alimentarse de objetos de tipo Planta.
	
	Crea un método en la clase Especie, el que tú decidas (dormir, comunicarse, tiempo de gestación,
	etc) y haz que tenga comportamientos distintos en cada clase; escribe en el Readme los detalles
	sobre el método que decidiste implementar.
"""

from random import randrange

class Especie(object):

	def __init__(self): pass

	def comunicarse(self):
		print("Hola")



class Herbivoro(Especie):

	def __init__(self):
		super(Herbivoro, self).__init__()

	def alimentarse(self, comida):
		if (isinstance(comida, Planta)):
			print("A comer!!!")
		else:
			print("No, solo como plantas ... pero gracias")

	def comunicarse(self):
		print("Hola, soy herbívoro")


class Carnivoro(Especie):

	def __init__(self):
		super(Carnivoro, self).__init__()

	def alimentarse(self, comida):
		# Carnı́voro, Herbı́voro y SerHumano
		if (isinstance(comida, Carnivoro) or isinstance(comida, Herbivoro) or isinstance(comida, SerHumano)):
			print("A comer!!!")
		else:
			print("Nooo... gracias.")

	def comunicarse(self):
		print("Hola, soy carnívoro")

class Leon(Carnivoro):

	def __init__(self):
		super(Leon, self).__init__()

	def comunicarse(self):
		print("Hola, soy un León carnívoro")

class Tiburon(Carnivoro):

	def __init__(self):
		super(Tiburon, self).__init__()

	def comunicarse(self):
		print("Hola, soy un Tiburón carnívoro")


class Jirafa(Herbivoro):

	def __init__(self):
		super(Jirafa, self).__init__()

	def comunicarse(self):
		print("Hola, soy una jirafa hervívora")

class Elefante(Herbivoro):

	def __init__(self):
		super(Elefante, self).__init__()

	def comunicarse(self):
		print("Hola, soy un Elefante hervívoro")

class SerHumano(Carnivoro, Herbivoro):

	def __init__(self): pass

	def alimentarse(self, comida):
		if (isinstance(comida, SerHumano)):
			print("No soy Canibal")
		else:
			print("A comer!!!")

	def comunicarse(self):
		print("Hola, soy un Ser Humano carnívoro y hervívoro pero no Canibal")

class Planta(object): pass

if __name__ == '__main__':
	
	alimentos = [Planta(), SerHumano(), Tiburon(), Carnivoro(), Jirafa()]

	print("\nComuniquensé!")
	aList = [SerHumano(), Carnivoro(), Herbivoro(), Tiburon(), Elefante()]
	for lo_que_sea in aList:
		lo_que_sea.comunicarse()

	print("\nComan algo!")
	for lo_que_sea in aList:
		aRandom = randrange(5)
		print("Si a un {} le dan para alimentarse {} éste dice: ".format(str(lo_que_sea.__class__.__name__), alimentos[aRandom].__class__.__name__))
		lo_que_sea.alimentarse(alimentos[aRandom])


