"""
	Usuario
	Clase que almacena los datos de nuestro usuario como lo son: el nombre de usuario, su contraseña,
	el total de juegos, los juegos ganados y los juegos perdidos
"""
class User(object):

	def __init__(self, user_name, password):
		self.user_name = user_name
		self.password = password
		self.total_games = 0
		self.games_won = 0
		self.games_lost = 0

	"""
		Reinicia los contadores de juegos
	"""
	def reset(self):
		self.total_games = 0
		self.games_won = 0
		self.games_lost = 0

	"""
		Regresa la constraseña del usuario
		@return
			La contraseña del usuario
	"""
	def get_password(self):
		return self.password

	"""
		Regresa el nombre del usuario
		@return
			El nombre del usuario
	"""
	def get_user_name(self):
		return self.user_name

	def get_total_games(self):
		return self.total_games

	def get_games_won(self):
		return self.games_won

	def get_games_lost(self):
		return self.games_lost
