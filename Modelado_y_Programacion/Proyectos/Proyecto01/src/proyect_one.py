from frames import *

if __name__ == '__main__':

	# Creamos la ventana
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