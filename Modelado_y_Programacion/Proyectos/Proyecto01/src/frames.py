import tkinter as tk
from tkinter import messagebox
from database import * 

"""
	Proyect_One
	Clase hija de Frame, con la cual organizamos los elementos que se mostrarán al usuario
	como primera ventana de nuestro programa.
	Con Proyect_One se muestra las dos opciones para ingresasr al programa, ya sea un inicio de sesión
	o la creación de una cuenta.
"""
class Proyect_One(tk.Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None):
		super(Proyect_One, self).__init__(master)
		self.pack()
		self.create_widgets()

	"""
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.register = tk.Button(self, height = 5, width = 50)
		self.register["text"] = "Registrar Jugador"
		self.register["command"] = self.method_register
		self.register.pack(side="top")

		self.login = tk.Button(self, height = 5, width = 50)
		self.login["text"] = "Iniciar Sesión"
		self.login["command"] = self.method_login
		self.login["fg"] = "#00820e"
		self.login.pack()

	"""
		Inicia un Register_Frame
	"""
	def method_register(self):
		aTK = tk.Tk()
		# Instanciamos el Frame
		new_register = SignUp_Frame(master=aTK)
		# Colocamos el título de nuestro Frame
		new_register.master.title("Crear Cuenta")
		# Con estos métodos obligamos a que la ventana no pueda cambiar sus dimensiones
		new_register.master.minsize(330, 120)
		new_register.master.maxsize(330, 120)
		# Iniciamos el Frame
		new_register.mainloop()

	"""
		Inicia un Login_Frame
	"""
	def method_login(self):
		aTK = tk.Tk()
		# Instanciamos el Frame
		new_login = Login_Frame(master=aTK)
		# Colocamos el título de nuestro Frame
		new_login.master.title("Iniciar Sesión")
		# Con estos métodos obligamos a que la ventana no pueda cambiar sus dimensiones
		new_login.master.minsize(330, 90)
		new_login.master.maxsize(330, 90)
		# Iniciamos el Frame
		new_login.mainloop()

"""

"""
class SignUp_Frame(tk.Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None):
		super(SignUp_Frame, self).__init__(master)
		self.pack()
		self.create_widgets()


	"""
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.frame1 = tk.Frame(self)
		self.frame1.pack()
		self.label1 = tk.Label(self.frame1, text="Nombre de Usuario", height=1, width=20)
		self.label1.pack(side="left")
		self.user_name_entry = tk.Entry(self.frame1, bd = 5)
		self.user_name_entry.pack(side="right")

		self.frame2 = tk.Frame(self)
		self.frame2.pack()
		self.label2 = tk.Label(self.frame2, text="Contraseña", height=1, width=20)
		self.label2.pack(side="left")
		self.password_entry = tk.Entry(self.frame2, bd = 5, show="*")
		self.password_entry.pack(side="right")

		self.frame3 = tk.Frame(self)
		self.frame3.pack()
		self.label3 = tk.Label(self.frame3, text="Contraseña", height=1, width=20)
		self.label3.pack(side="left")
		self.password_confirm_entry = tk.Entry(self.frame3, bd = 5, show="*")
		self.password_confirm_entry.pack(side="right")

		self.enter_btn = tk.Button(self, height=1, width=30)
		self.enter_btn["text"] = "Iniciar sesión"
		self.enter_btn["command"] = self.sign_up
		self.enter_btn.pack()

	def sign_up(self):
		user_name = self.user_name_entry.get()
		password = self.password_entry.get()
		password_confirm = self.password_confirm_entry.get()

		if (user_name == "" or password == "" or password_confirm == ""):
			self.show_error(message="Favor de introducir todos los campos.")
		elif (" " in user_name):
			self.show_error(message="Tu nombre de usuario no puede tener espacios en blanco.")
		elif (" " in password):
			self.show_error(message="Tu contraseña no puede tener espacios en blanco.")
		elif (password != password_confirm):
			self.show_error(message="Las contraseñas no coinciden.")
		else:
			database = Database()
			try:
				database.new_user(user_name, password)
				print("sign_up")
			except UserAlreadyExists:
				self.show_error(message="El nombre de usuario ya ha sido registrado, intenta otro.")

	"""
		Muestra un error
		@param title
			Título del error
		@param message
			Mensaje que se muestra de error
	"""
	def show_error(self, title="Error", message="Error"):
		messagebox.showerror(title, message)


"""
	Login_Frame
	Clase hija de Frame, con la cual organizamos los elementos que se mostrarán al usuario
	para que pueda iniciar sesión en nuestro programa.
	Con Login_Frame se muestran los dos campos para ingresasr el nombre de usuario y la contraseña
	para así poder iniciar sesión.
"""
class Login_Frame(tk.Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None):
		super(Login_Frame, self).__init__(master)
		self.pack()
		self.create_widgets()


	"""
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.frame1 = tk.Frame(self)
		self.frame1.pack()
		self.label1 = tk.Label(self.frame1, text="Nombre de Usuario", height=1, width=20)
		self.label1.pack(side="left")
		self.user_name_entry = tk.Entry(self.frame1, bd = 5)
		self.user_name_entry.pack(side="right")

		self.frame2 = tk.Frame(self)
		self.frame2.pack()
		self.label2 = tk.Label(self.frame2, text="Contraseña", height=1, width=20)
		self.label2.pack(side="left")
		self.password_entry = tk.Entry(self.frame2, bd = 5, show="*")
		self.password_entry.pack(side="right")

		self.enter_btn = tk.Button(self, height=1, width=30)
		self.enter_btn["text"] = "Iniciar sesión"
		self.enter_btn["command"] = self.login
		self.enter_btn.pack()


	"""
		Verifica si los campos de entrada son válidos, si lo son el usuario entrará a nuestro programa,
		en caso contrario se mostrará una ventana de error.
	"""
	def login(self):
		user_name = (self.user_name_entry.get()).strip()
		password = (self.password_entry.get()).strip()

		if (user_name == "" or password == ""):
			self.show_error(message="Favor de introducir todos los campos")
		else:
			database = Database()
			if (not database.have_user(user_name)):
				self.show_error(title="Nombre de usuario", message="Nombre de usuario incorrecto")
			elif (not database.correct_password(user_name, password)):
				self.show_error(title="Contraseña", message="Contraseña incorrecta")
			else:
				user = database.get_user(user_name)
				print("Login succefull")

	"""
		Muestra un error
		@param title
			Título del error
		@param message
			Mensaje que se muestra de error
	"""
	def show_error(self, title="Error", message="Error"):
		messagebox.showerror(title, message)
