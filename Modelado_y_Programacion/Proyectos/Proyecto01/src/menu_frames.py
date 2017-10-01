"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Proyectos/Proyecto01/src/menu_frames.py
"""

import tkinter as tk
from tkinter import messagebox
from database import * 
from game import *
import time
import os 

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
		main_frame = tk.Frame(self, bg="#BED6EF")
		main_frame.pack()

		# Obtenemos la ruta a nuestra imagen de inicio
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.dir_path += "/Images/rem_background.png"

		rem_image = tk.PhotoImage(master=self, file=self.dir_path)
		self.background_image = tk.Label(main_frame, bg="#BED6EF", image=rem_image, height=600, width=300)
		self.background_image.image = rem_image
		self.background_image.bg = "#BED6EF"
		self.background_image.pack(side="right")

		self.options_frame = tk.Frame(main_frame, bg="#BED6EF", width=650)
		self.label_info = tk.Label(self.options_frame, text="Inicia sesión\no\ncrea una cuenta\npara ingresar a\n¡REM-MEMORAMA!\n", bg="#BED6EF", font=("Courier", 20))
		self.label_info.pack()
		self.register = tk.Button(self.options_frame, text="Registrar Jugador", command=self.method_register, height=4, width=50)
		self.register.pack()
		self.login = tk.Button(self.options_frame, text="Iniciar Sesión", command=self.method_login, height=4, width=50)
		self.login["fg"] = "#00820e"
		self.login.pack()
		self.options_frame.pack(side="left")
		

	"""
		Inicia un Register_Frame
	"""
	def method_register(self):
		aTK = tk.Tk()
		# Instanciamos el Frame
		new_register = SignUp_Frame(master=aTK, frames_to_close=[self])
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
		new_login = Login_Frame(master=aTK, frames_to_close=[self])
		# Colocamos el título de nuestro Frame
		new_login.master.title("Iniciar Sesión")
		# Con estos métodos obligamos a que la ventana no pueda cambiar sus dimensiones
		new_login.master.minsize(330, 90)
		new_login.master.maxsize(330, 90)
		# Iniciamos el Frame
		new_login.mainloop()

"""
	SignUp_Frame
	Clase hija de Frame, con la cual organizamos los elementos que se mostrarán al usuario
	para que pueda crear una cuenta en nuestro programa.
	Con SignUp_Frame se muestran tres campos para ingresasr el nombre de usuario, la contraseña
	y confirmación de contraseña para así poder crear la cuenta.
"""
class SignUp_Frame(tk.Frame):

	"""
		Constructor
		@param frame
			Frames que tendremos que cerrar en cuanto el Menu_Frame inicie
	"""
	def __init__(self, master=None, frames_to_close=[]):
		super(SignUp_Frame, self).__init__(master)
		self.frames_to_close = frames_to_close
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

	"""
		Verifica los campos para ver si son válidos y dar de alta un usuario.
		Si todos los datos son correctos se abre automaticamente la ventana del menú principal.
		Si los datos no son correctos se muestra el mensaje de error correspondiente
	"""
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
				#Si el registro fue éxitoso ingresaremos a la pantalla principal
				user = database.get_user(user_name)
				messagebox.showinfo("Éxito", "Cuenta creada con éxito")
				aTK = tk.Tk()
				self.frames_to_close.append(self)
				menu_frame = Menu_Frame(aTK, frames_to_close=self.frames_to_close, user=user)
				menu_frame.master.title("Bienvenido a ¡Rem-Memorama!")
				menu_frame.master.maxsize(680, 480)
				menu_frame.master.minsize(680, 480)
				menu_frame.mainloop()
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
	def __init__(self, master=None, frames_to_close=[]):
		super(Login_Frame, self).__init__(master)
		self.frames_to_close = frames_to_close
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
		user_name = self.user_name_entry.get()
		password = self.password_entry.get()

		if (" " in user_name):
			self.show_error(message="Tu nombre de usuario no puede tener espacios en blanco.")
		elif (" " in password):
			self.show_error(message="Tu contraseña no puede tener espacios en blanco.")
		elif (user_name == "" or password == ""):
			self.show_error(message="Favor de introducir todos los campos")
		else:
			database = Database()
			if (not database.have_user(user_name)):
				self.show_error(title="Nombre de usuario", message="Nombre de usuario incorrecto")
			elif (not database.correct_password(user_name, password)):
				self.show_error(title="Contraseña", message="Contraseña incorrecta")
			else:
				user = database.get_user(user_name)
				aTK = tk.Tk()
				self.frames_to_close.append(self)
				menu_frame = Menu_Frame(aTK, frames_to_close=self.frames_to_close, user=user)
				menu_frame.master.title("Bienvenido a ¡Rem-Memorama!")
				menu_frame.master.maxsize(680, 480)
				menu_frame.master.minsize(680, 480)
				menu_frame.mainloop()

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
	Menú principal del programa.
	En éste frame existen las opciones para iniciar un juego nuevo, para ver las estadísticas y para poder borrar su historial
"""
class Menu_Frame(tk.Frame):

	"""
		Constructor
		@param frames
			Lista que contiene los Frames que tendremos que cerrar cuando inicie éste menú
	"""
	def __init__(self, master=None, frames_to_close=[], user=None):
		super(Menu_Frame, self).__init__(master)
		for frame in frames_to_close:
			frame.master.destroy()
		self.user = user
		self.pack()
		self.create_widgets()

	""" 
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.main_frame = tk.Frame(self, bg="#ffffff")
		self.main_frame.pack()

		# GIF
		######################################################################################
		# Obtenemos la ruta a nuestro gif de inicio
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.dir_path += "/Images/rem.gif"
		# Iniciamos la animacion de nuestro gif
		self.rem_gif = tk.PhotoImage(master=self, file=self.dir_path, format="gif -index 1")
		self.label_gif = tk.Label(self.main_frame, image=self.rem_gif)
		self.label_gif.image = self.rem_gif
		self.label_gif.pack(side="left")
		self.run_animation()
		######################################################################################
		# Menu
		self.options_frame = tk.Frame(self.main_frame, bg="#ffffff")
		self.label_title = tk.Label(self.options_frame, bg="#ffffff", text="REM\n¡MEMORAMA!", font=("Courier", 44))
		self.label_title.pack()
		self.play_btn = tk.Button(self.options_frame, text="Jugar", command=self.play, bd=5, font=("Arial", 20), height=2, width=50)
		self.play_btn.pack()
		self.statistics_btn = tk.Button(self.options_frame, text="Estadísticas", bd=5, font=("Arial", 20), command=self.estadistics, height=2, width=50)
		self.statistics_btn.pack()
		self.clear_btn = tk.Button(self.options_frame, text="Borrar historial", bd=5, font=("Arial", 20), command=self.clear, height=2, width=50)
		self.clear_btn.pack()
		self.options_frame.pack(side="right")


	"""
		Se ejecuta cuando se preciona el botón de JUGAR.
		Inicia un Game_Frame
	"""
	def play(self): 
		aTK = tk.Tk()
		game_frame = Game_Frame(aTK, user=self.user)
		game_frame.master.title("¡REM-MEMORAMA!")
		game_frame.master.maxsize(600, 400)
		game_frame.master.minsize(600, 400)
		game_frame.mainloop()

	"""
		Se ejecuta cuando se preciona el botón de ESTADÍSTICAS.
		Inicia un Estadistics_Frame
	"""
	def estadistics(self):
		aTK = tk.Tk()
		estadistics_frame = Estadistics_Frame(aTK, user=self.user)
		estadistics_frame.master.title("Estadísticas")
		estadistics_frame.master.maxsize(330, 400)
		estadistics_frame.master.minsize(330, 400)
		estadistics_frame.mainloop()


	"""
		Se ejecuta cuando se preciona el botón de BORRAR HISTORIAL.
		Inicia un Clear_Frame
	"""
	def clear(self): 
		aTK = tk.Tk()
		clear_frame = Clear_Frame(aTK, user=self.user)
		clear_frame.master.title("Borrar historial")
		clear_frame.master.maxsize(400, 100)
		clear_frame.master.minsize(400, 100)
		clear_frame.mainloop()


	"""
		Guardamos en frames todas las imagenes que tiene nuestro gif
	"""
	def run_animation(self):
		self.frames = [tk.PhotoImage(master=self, file=self.dir_path, format="gif -index {}".format(i)) for i in range(26)]
		self.label_gif.after(0, self.change_image, 0)


	"""
		Cambiamos la imagen de nuestro gif cada 80 miliseguntos para tener continuidad en nuestro gif
	"""
	def change_image(self, index_frame):
		# 26 son el número de frames de nuestro gif, cuando llegue a ese punto reiniciamos las imagenes
		if (index_frame != 26):
			self.rem_gif = self.frames[index_frame]
			self.label_gif.config(image=self.rem_gif)
			self.label_gif.image = self.rem_gif
			self.label_gif.pack(side="left")
			index_frame += 1
			self.label_gif.after(50, self.change_image, index_frame)
		else:
			self.label_gif.after(0, self.change_image, 0)



class Estadistics_Frame(tk.Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None, user=None):
		super(Estadistics_Frame, self).__init__(master)
		self.user = user
		self.pack()
		self.create_widgets()

	"""
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.label_user_name = tk.Label(master=self, text=self.user.get_user_name(), font=("Courier", 30), height=2, width=25) 
		self.label_user_name.pack()
		self.label_total_games = tk.Label(master=self, text="Juegos totales: {}".format(self.user.get_total_games()), font=("Arial", 12), height=4, width=25) 
		self.label_total_games.pack()
		self.label_games_won = tk.Label(master=self, text="Juegos ganados: {}".format(self.user.get_games_won()), font=("Arial", 12), height=4, width=30) 
		self.label_games_won.pack()
		self.label_games_lost = tk.Label(master=self, text="Juegos perdidos: {}".format(self.user.get_games_lost()), font=("Arial", 12), height=4, width=30) 
		self.label_games_lost.pack()
		self.btn_close = tk.Button(master=self, text="OK", command=self.close, fg="red", height=2, width=20)
		self.btn_close.pack()

	"""
		Cierra éste Frame
	"""
	def close(self):
		self.master.destroy()



class Clear_Frame(tk.Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None, user=None):
		super(Clear_Frame, self).__init__(master)
		self.user = user
		self.pack()
		self.create_widgets()

	"""
		Organiza los elementos dentro de nuestro Frame
	"""
	def create_widgets(self):
		self.label_info = tk.Label(master=self, text="¿Seguro quieres borrar tu historial?", font=("Arial", 14), height=2, width=80)
		self.label_info.pack()
		self.aFrame = tk.Frame(master=self)
		self.ok_btn = tk.Button(self.aFrame, text="Sí, borrar.", command=self.clear, width=12, fg="green")
		self.ok_btn.pack(side="left")
		self.cancel_btn = tk.Button(self.aFrame, text="Cancelar.", command=self.close, width=12, fg="red")
		self.cancel_btn.pack(side="right")
		self.aFrame.pack()

	"""
		Reinicia las estadísticas de juego y lo actualiza en la base de datos
	"""
	def clear(self):
		aDatabase = Database()
		self.user.reset()
		aDatabase.update_user(self.user)
		messagebox.showinfo("Completado", "Historial borrado")
		self.close()

	"""
		Cierra éste Frame
	"""
	def close(self):
		self.master.destroy()