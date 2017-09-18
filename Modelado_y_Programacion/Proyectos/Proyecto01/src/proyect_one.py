import tkinter as tk

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
		print("register")

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
		print("Login method")

if __name__ == '__main__':
	
	root = tk.Tk()

	# Creamos el Frame de inicio
	app = Proyect_One(master=root)
	# Asignamos el título
	app.master.title("Proyecto 1: Memorama")
	# Evitamos el cambio de dimensiones de la ventana
	app.master.minsize(300,170)
	app.master.maxsize(300,170)
	# Mostramos el Frame
	app.mainloop()
