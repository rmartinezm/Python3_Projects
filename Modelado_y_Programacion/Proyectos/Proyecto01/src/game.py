"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Proyectos/Proyecto01/src/game.py
"""

from database import *
import tkinter as tk
from tkinter import Frame
from tkinter import Button
from tkinter import Tk
from tkinter import messagebox
from random import randrange

class Game_Frame(Frame):

	"""
		Constructor
	"""
	def __init__(self, master=None, user=None):
		super(Game_Frame, self).__init__(master)
		self.user = user
		self.flag = False
		self.last_btn_presed = None
		self.num_errors = 0
		# Creamos nuestro objeto Game
		self.game = Game()
		self.database = Database()

		self.pack()
		self.create_widgets()
		self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9, self.btn_10, self.btn_11, self.btn_12, self.btn_13, self.btn_14, self.btn_15, self.btn_16]


	"""
		Organiza los elementos dentro del Frame
	"""
	def create_widgets(self):
		self.main_label = tk.Label(master=self, text="¡REM-MEMORAMA!", font=("Courier", 20))
		self.main_label.pack()
		# Primer nivel del memorama
		self.first_line = Frame(self)
		self.btn_1 = Button(master=self.first_line, text="1", height=4, width=15)
		self.btn_1["command"] =  lambda:self.revel(1, self.btn_1)
		self.btn_1.pack(side="left")
		self.origin_color = self.btn_1["bg"]
		self.origin_font = self.btn_1["font"]
		self.btn_2 = Button(master=self.first_line, text="2", height=4, width=15)
		self.btn_2["command"] =  lambda:self.revel(2, self.btn_2)
		self.btn_2.pack(side="left")
		self.btn_3 = Button(master=self.first_line, text="3", height=4, width=15)
		self.btn_3["command"] =  lambda:self.revel(3, self.btn_3)
		self.btn_3.pack(side="left")
		self.btn_4= Button(master=self.first_line, text="4", height=4, width=15)
		self.btn_4["command"] =  lambda:self.revel(4, self.btn_4)
		self.btn_4.pack(side="left")
		self.first_line.pack()
		# Segundo nivel del memorama
		self.second_line = Frame(self)
		self.btn_5 = Button(master=self.second_line, text="5", height=4, width=15)
		self.btn_5["command"] =  lambda:self.revel(5, self.btn_5)
		self.btn_5.pack(side="left")
		self.btn_6 = Button(master=self.second_line, text="6", height=4, width=15)
		self.btn_6["command"] =  lambda:self.revel(6, self.btn_6)
		self.btn_6.pack(side="left")
		self.btn_7 = Button(master=self.second_line, text="7", height=4, width=15)
		self.btn_7["command"] =  lambda:self.revel(7, self.btn_7)
		self.btn_7.pack(side="left")
		self.btn_8 = Button(master=self.second_line, text="8", height=4, width=15)
		self.btn_8["command"] =  lambda:self.revel(8, self.btn_8)
		self.btn_8.pack(side="left")
		self.second_line.pack()
		# Tercer nivel del memorama
		self.third_line = Frame(self)
		self.btn_9 = Button(master=self.third_line, text="9", height=4, width=15)
		self.btn_9["command"] =  lambda:self.revel(9, self.btn_9)
		self.btn_9.pack(side="left")
		self.btn_10 = Button(master=self.third_line, text="10", height=4, width=15)
		self.btn_10["command"] =  lambda:self.revel(10, self.btn_10)
		self.btn_10.pack(side="left")
		self.btn_11 = Button(master=self.third_line, text="11", height=4, width=15)
		self.btn_11["command"] =  lambda:self.revel(11, self.btn_11)
		self.btn_11.pack(side="left")
		self.btn_12 = Button(master=self.third_line, text="12", height=4, width=15)
		self.btn_12["command"] =  lambda:self.revel(12, self.btn_12)
		self.btn_12.pack(side="left")
		self.third_line.pack()
		# Cuarto nivel del memorama
		self.fourth_line = Frame(self)
		self.btn_13 = Button(master=self.fourth_line, text="13", height=4, width=15)
		self.btn_13["command"] =  lambda:self.revel(13, self.btn_13)
		self.btn_13.pack(side="left")
		self.btn_14 = Button(master=self.fourth_line, text="14", height=4, width=15)
		self.btn_14["command"] =  lambda:self.revel(14, self.btn_14)
		self.btn_14.pack(side="left")
		self.btn_15 = Button(master=self.fourth_line, text="15", height=4, width=15)
		self.btn_15["command"] =  lambda:self.revel(15, self.btn_15)
		self.btn_15.pack(side="left")
		self.btn_16 = Button(master=self.fourth_line, text="16", height=4, width=15)
		self.btn_16["command"] =  lambda:self.revel(16, self.btn_16)
		self.btn_16.pack(side="left")
		self.fourth_line.pack()
		# Errores
		self.label_errors = tk.Label(self, text="Errores: {}".format(self.num_errors), font=("Courier", 20), fg="red")
		self.label_errors.pack()

	"""
		Revela la opción seleccionada
	"""
	def revel(self, index, btn_presed=None):
		# Si ya hay una casilla seleccionada
		if (self.flag):
			btn_presed["bg"] = "#BED6EF"
			btn_presed["state"] = "disabled"
			btn_presed["text"] = str(self.game.cards_dictionary[index-1])
			btn_presed["font"] = ("Arial", 20)
			btn_presed["height"] = 2
			btn_presed["width"] = 8
			if (btn_presed["text"] == self.last_btn_presed["text"]):
				messagebox.showinfo("Correcto", "Bien!")
				self.last_btn_presed["bg"] = "#0eb711"
				btn_presed["bg"] = "#0eb711"
				self.last_btn_presed = None
				self.flag = False

				won = True
				for button in self.buttons:
					if (button["bg"] == self.origin_color):
						won = False
				if (won):
					self.won_game()
			else:
				self.num_errors += 1
				self.label_errors["text"] = "Errores {}".format(self.num_errors)
				if (self.num_errors == 3):
					self.lost_game()
				else:
					messagebox.showinfo("Incorrecto", "Lo siento!")
					self.last_btn_presed["bg"] = self.origin_color
					self.last_btn_presed["state"] = "normal"
					self.last_btn_presed["text"] = self.last_btn_presed_text
					self.last_btn_presed["font"] = self.origin_font
					self.last_btn_presed["height"] = 4
					self.last_btn_presed["width"] = 15
					btn_presed["bg"] = self.origin_color
					btn_presed["text"] = str(index)
					btn_presed["font"] = self.origin_font
					btn_presed["state"] = "normal"
					btn_presed["height"] = 4
					btn_presed["width"] = 15
					self.last_btn_presed = None
					self.flag = False	
		else:
			self.flag = True
			self.last_btn_presed_text = btn_presed["text"]
			btn_presed["bg"] = "#BED6EF"
			btn_presed["state"] = "disabled"
			btn_presed["text"] = str(self.game.cards_dictionary[index-1])
			btn_presed["font"] = ("Arial", 20)
			btn_presed["height"] = 2
			btn_presed["width"] = 8
			self.last_btn_presed = btn_presed


	"""
		Muestra al usuario que ganó y se actualizan los datos
	"""
	def won_game(self):
		messagebox.showinfo("¡Ganaste!", "¡Felicidades!")
		self.user.total_games += 1
		self.user.games_won += 1
		self.database.update_user(self.user)
		self.master.destroy()

	"""
		Muestra al usuario que perdió y se actualizan los datos
	"""
	def lost_game(self):
		messagebox.showinfo("¡Perdiste!", "¡Lo siento!")
		self.user.total_games += 1
		self.user.games_lost += 1
		self.database.update_user(self.user)
		self.master.destroy()


"""
	Objeto Game.
	Simula un memorama
"""
class Game(object):

	"""
		Constructor
	"""
	def __init__(self):
		self.cards_dictionary = {}
		self.new_game()
		self.wrongs = 0
		self.finished = False

	"""
		Coloca aleatoreamente los símbolos para el memorama
	"""
	def new_game(self):
		symbols = [u'\u2603', u"\u2604", u"\u2605", u"\u2606", u'\u2600', u'\u2602', u'\u262F', u'\u2660']
		for i in range(16):
			random_symbol = symbols[randrange(len(symbols))]
			# A lo más entra al diccionario 2 veces un símbolo
			if (random_symbol in self.cards_dictionary.values()):
				symbols.remove(random_symbol)	
			self.cards_dictionary[i] = random_symbol
