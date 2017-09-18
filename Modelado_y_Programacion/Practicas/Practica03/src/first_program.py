'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica03/src/first_program.py

	Crea una clase llamada Videojuego, un videojuego tiene: nombre, género, precio y desarrollador.
	Realiza lo siguiente: Crea un constructor que inicialice los atributos anteriores, asegúrate de evitar
	que haya precios menores a $0 Crea un método toString() para imprimir objetos de tipo Videojuego
	de la siguiente forma:

		Nombre: The last of us
		Género: Survival horror, aventuras
		Precio: $999.99
		Desarrollador: Naughty Dog
		
	Instancia 10 objetos de tipo Videojuego
	Crea los siguientes métodos:
		elMasCaro(self)
		Método llamado que regrese el objeto de tipo videojuego que sea el de mayor costo en la tienda
		(puede haber dos videosjuegos o más que sean los de mayor costo)
		rebajaVideojuego(self, vj)
		Método que recibe un objeto de tipo videojuego y lo rebaja un 15 % de su costo original.
		getJuegosPorCompania(self)
		Método que regresa todos los tı́tulos que pertenecen a las diferentes compañı́as que haya
		getJuegosPorGenero(self, genero) Método que regresa todos los juegos que pertenezcan a la
		categorı́a genero que recibe el método como parámetro
'''

from random import randrange

'''
	Clase Videojuego.
	Un videojuego tiene un nombre, género, precio y desarrollador.
'''
class Videojuego(object):

	'''
		Constructor de un videojuego.
		@param nombre
			Nombre del videojuego
		@param genero
			El género del videojuego
		@param precio
			El precio del videojuego
		@param desarrollador
			El desarrollador del videojuego
	'''
	def __init__(self, nombre, genero, precio, desarrollador):
		self.nombre = nombre
		self.genero = genero
		self.desarrollador = desarrollador
		if (precio < 0):
			raise InvalidParametersException()
		self.precio = precio


	'''
		Imprime el videojuego con un formato en específico
	'''
	def toString(self):
		print("Nombre: {}\nGénero: {}\nPrecio: {}\nDesarrollador: {}".format(self.nombre, self.genero, self.precio, self.desarrollador))


	'''
		Regresa la representación en cadena del videojuego
		@return
			La representación en cadena del videojuego
	'''
	def __str__(self):
		return "Nombre: {}\nGénero: {}\nPrecio: {}\nDesarrollador: {}\n".format(self.nombre, self.genero, self.precio, self.desarrollador)

'''
	Clase GameStore
	Clase con la cual accedemos a métodos que trabajan con una lista de videojuegos
'''
class GameStore(object):

	'''	
		Contructor que recibe una lista con los videojuegos con los que cuenta la tienda
		@param videogames
			Lista de videojuegos de la tienda
	'''
	def __init__(self, videogames):
		self.videogames = videogames


	'''
		Regresa una lista con los videojuegos más caros de la tienda
		@return
			Una Lista con los videojuegos más caros
	'''
	def elMasCaro(self):
		the_most_expensive = self.videogames[0]
		for v in self.videogames:
			the_most_expensive = v if (v.precio > the_most_expensive.precio) else the_most_expensive
		aList = []
		for v in self.videogames:
			if v.precio == the_most_expensive.precio:
				aList.append(v)
		return aList  


	'''
		Método que recibe un objeto de tipo videojuego y lo rebaja un 15 % de su costo original.
		@param videogame
			Videojuego al que rebajaremos el precio
	'''
	def rebajaVideojuego(self, videogame):
		videogame.precio -= (videogame.precio * .15)

	'''
		Regresa todos los tı́tulos que pertenecen a las diferentes compañı́as que haya
		@return 
			Un diccionario con listas de videojuegos que pertenecen a la compañía que se desea.
			Las Keys del diccionario son las compañías disponibles y los Values son las listas con videojuegos 
	'''
	def getJuegosPorCompania(self):
		aDicctionary = {}
		for videogame in videogames:
			compania = videogame.desarrollador;
			if compania in aDicctionary:
				aList = aDicctionary.get(compania)
				aList.append(videogame)
				aDicctionary[compania] = aList
			else:
				aDicctionary[compania] = [videogame]
		return aDicctionary


	'''
		Regresa todos los juegos que pertenezcan al género que recibe el método como parámetro
		@param genero
			El género de videojuegos que se desea
		@return
			Una lista con los videojuegos que sean del gérero deseado

	'''
	def getJuegosPorGenero(self, genero):
		aList = []
		for videogame in videogames:
			if videogame.genero.upper() == genero.upper():
				aList.append(videogame)
		return aList


'''
	Excepción que ocuparemos para indicar que los prametros no son válidos
'''
class InvalidParametersException(Exception): pass


if __name__ == '__main__':
	
	# Instancias de Videojuego
	v1 = Videojuego("Grand Theft Auto V", "Acción-Aventura", 850.00, "Rockstar North")
	v2 = Videojuego("Super Mario Bros", "Plataformas", 100.00, "Nintendo EAD")
	v3 = Videojuego("The Elder Scrolls V: Skyrim", "Rol de acción", 800.00, "Bethesda Game Studios")
	v4 = Videojuego("Minecraft", "Sandbox", 480.00, "Mojang AB")
	v5 = Videojuego("BioShock", "FPS", 500.00, "2K Boston")
	v6 = Videojuego("Half-Life 2", "Acción en primera persona", 820.00, "Valve")
	v7 = Videojuego("Metroid", "Acción-Aventura", 850.00, "Nintendo R&D1")
	v8 = Videojuego("The Last of Us", "Survival horror", 200.00, "Naughty Dog")
	v9 = Videojuego("Portal", "Lógica", 320.00, "Valve Corporation")
	v10 = Videojuego("Red Dead Redemption", "Disparos en tercera persona", 850.00, "Rockstar North")

	# Lista de Videojuegos
	videogames = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
	print("Todos los videojuegos:")
	aString = ""
	for videogame in videogames:
		aString += videogame.nombre + ", "
	if aString != "":
		aString = aString[:len(aString)-2] 
	print(aString)
	# Tienda de Videojuegos
	game_store = GameStore(videogames)

	# elMasCaro
	print("\nLos videojuegos más caros son: ")
	aList = game_store.elMasCaro()
	aString = ""
	for videogame in aList:
		aString += videogame.nombre + ", "
	if aString != "":
		aString = aString[:len(aString)-2] 
	print(aString)

	# Rebaja Videojuego
	aVideogame = videogames[randrange(10)]
	print("\nEl videojuego antes de la rebaja: ")
	aVideogame.toString()
	game_store.rebajaVideojuego(aVideogame)
	print("\nEl videojuego despues de la rebaja: ")
	aVideogame.toString()

	# getJuegosPorCompania
	aDicctionary = game_store.getJuegosPorCompania()
	print("\nLos juegos de la Compañía Rockstar North son: ")
	aList = aDicctionary.get("Rockstar North", [])
	aString = ""
	for videogame in aList:
		aString += videogame.nombre + ", "
	if aString != "":
		aString = aString[:len(aString)-2] 
	print(aString + "\n")


	# getJuegosPorGenero
	aList = game_store.getJuegosPorGenero("Acción-Aventura")
	print("Lista con los juegos del género Acción-Aventura: ")
	aString = ""
	for videogame in aList:
		aString += videogame.nombre + ", "
	if aString != "":
		aString = aString[:len(aString)-2] 
	print(aString + "\n")


