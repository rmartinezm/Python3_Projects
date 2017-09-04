'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica03/first_program.py

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

'''

'''
class Videojuego(object):

	'''

	'''
	def __init__(self, nombre, genero, precio, desarrollador):
		self.nombre = nombre
		self.genero = genero
		self.desarrollador = desarrollador
		if (precio < 0):
			raise InvalidParametersException()
		self.precio = precio


	'''

	'''
	def toString(self):
		print("Nombre: {}\nGénero: {}\nPrecio: {}\nDesarrollador: {}".format(self.nombre, self.genero, self.precio, self.desarrollador))


	'''

	'''
	def __str__(self):
		return "Nombre: {}\nGénero: {}\nPrecio: {}\nDesarrollador: {}\n".format(self.nombre, self.genero, self.precio, self.desarrollador)

'''

'''
class GameStore(object):

	'''

	'''
	def __init__(self, videogames):
		self.videogames = videogames


	'''

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

	'''
	def rebajaVideojuego(self, videogame):
		price_with_discount = videogame.precio - (videogame.precio * .15)
		print(price_with_discount)

	'''

	'''
	def getJuegosPorCompania(self):
		pass


	'''

	'''
	def getJuegosPorGenero(self, genero):
		pass


'''

'''
class InvalidParametersException(Exception): pass


if __name__ == '__main__':
	
	v1 = Videojuego("Grand Theft Auto V", "Acción-Aventura", 850.00, "Rockstar North")
	v2 = Videojuego("Super Mario Bros", "Plataformas", 100.00, "Nintendo EAD")
	v3 = Videojuego("The Elder Scrolls V: Skyrim", "Rol de acción", 800.00, "Bethesda Game Studios")
	v4 = Videojuego("Minecraft", "Sandbox", 480.00, "Mojang AB")
	v5 = Videojuego("BioShock", "FPS", 500.00, "2K Boston")
	v6 = Videojuego("Half-Life 2", "Acción en primera persona", 820.00, "Valve")
	v7 = Videojuego("Metroid", "Acción-aventura", 850.00, "Nintendo R&D1")
	v8 = Videojuego("The Last of Us", "Survival horror", 200.00, "Naughty Dog")
	v9 = Videojuego("Portal", "Lógica", 320.00, "Valve Corporation")
	v10 = Videojuego("Red Dead Redemption", "Disparos en tercera persona", 800.00, "Rockstar North")

	videogames = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
	game_store = GameStore(videogames)

	v1.toString()
	game_store.rebajaVideojuego(v1)


