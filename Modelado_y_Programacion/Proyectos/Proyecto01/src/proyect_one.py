"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Proyectos/Proyecto01/src/proyect_one.py
"""
from menu_frames import *

if __name__ == '__main__':
	# Creamos la ventana
	root = tk.Tk()
	# Creamos el Frame de inicio
	app = Proyect_One(master=root)
	# Asignamos el título
	app.master.title("Proyecto 1: Memorama")
	# Evitamos el cambio de dimensiones de la ventana
	app.master.minsize(650,400)
	app.master.maxsize(650,400)
	# Mostramos el Frame
	app.mainloop()