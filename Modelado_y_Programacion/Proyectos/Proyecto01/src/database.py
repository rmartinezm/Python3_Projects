"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Proyectos/Proyecto01/src/database.py
"""

import shelve
from user_class import User

class Database(object):

	def __init__(self):
		self.database = shelve.open("default_database")

	"""
		Nos indica si existe un usuario con el nombre que se recibe como parametro
		@param user_name
			Nombre del usuario que buscaremos en la base de datos
		@return 
			True si el usuario ya está registrado en la base de datos
			False en otro caso
	"""
	def have_user(self, user_name):
		return user_name in self.database

	"""
		Nos indica si la contraseña es correcta para el nombre de usuario que se recibe 
		como parametro.
		@param user_name
			El nombre de usuario del que corroboraremos la contraseña.
		@param password
			Contraseña que verificaremos sea correcta
		@return 
			True si la contraseña coinside
			False en otro caso
 	"""
	def correct_password(self, user_name, password):
		return (self.database[user_name]).get_password() == password

	"""
		Regresa el objeto Usuario que tenga el mismo nombre de usuario del que se recibe como parametro.
		@param user_name
			El nombre de usuario que buscamos.
		@return 
			El usuario con ese mismo nombre de usuario.
			None si el usuario no está en la base de datos.
	"""
	def get_user(self, user_name):
		try:
			user = self.database[user_name]
			return user
		except:
			return None

	"""
		Agrega un nuevo usuario a la base de datos
		@param user_name
			Nombre de usuario deseado
		@param password
			Constraseña deseada
		@raise UserAlreadyExists
			Si el nombre de usuario ya está en la base de datos
	"""
	def new_user(self, user_name, password):
		if (self.have_user(user_name)):
			raise UserAlreadyExists()
		else:
			user = User(user_name, password)
			self.database[user_name] = user

	"""
		Actualiza un usuario en la base de datos
		@param user
			Usuario que actualizaremos
	"""
	def update_user(self, user):
		self.database[user.get_user_name()] = user

"""
	Exception para indicar que un usuario ya existe en la base de datos
"""
class UserAlreadyExists(Exception): pass 