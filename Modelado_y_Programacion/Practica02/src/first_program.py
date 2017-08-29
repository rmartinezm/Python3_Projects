'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica02/first_program.py

	Escribe funciones que permitan convertir numeros:
		* De decimal a octal y de octal a decimal
	 	* De octal a hexadecimal y hexadecimal a octal
'''

import math

def octal_to_decimal(num_octal):
	n = 0
	num_decimal = 0
	is_negative = float(num_octal) < 0

	sOctal = str(math.fabs(float(num_octal)))

	aList = sOctal.split(".")

	sOctal = aList[0][::-1]
	decimal_part = aList[1]

	for number in sOctal:
		if (int(number) > 7):
			raise NumberException()

		num_decimal += int(number) * (8 ** n)
		n += 1

	n = -1
	for number in decimal_part:
		if (int(number) > 7):
			raise NumberException()

		num_decimal += int(number) * (8 ** n)
		n -= 1

	return num_decimal * (-1) if is_negative else num_decimal


def decimal_to_octal(num_decimal):
	is_negative = num_decimal < 0
	r_binary = decimal_to_binary(math.fabs(num_decimal))[::-1]

	octal_number = ""

	aux_list = []

	for number in r_binary:
		if (len(aux_list) == 3):
			octal = int(aux_list[0]) * 4
			octal += int(aux_list[1]) * 2
			octal += int(aux_list[2]) * 1
			octal_number = str(octal) + octal_number
			aux_list = [number]
		else:
			aux_list.insert(0, number)

	if(aux_list != []):
		while len(aux_list) != 3:
			aux_list.insert(0, "0")
		octal = int(aux_list[0]) * 4
		octal += int(aux_list[1]) * 2
		octal += int(aux_list[2]) * 1
		octal_number = str(octal) + octal_number

	return int(octal_number) * -1 if is_negative else int(octal_number)



def octal_to_hexadecimal(num_octal):
	pass

def hexadecimal_to_octal(num_hexadecimal):
	pass

def decimal_to_binary(num_decimal):
	binary = ""
	
	aux = num_decimal

	while 1:
		aux_uno = aux // 2
		binary += "1" if aux_uno * 2 != aux else "0"
		aux = aux_uno
		if (aux_uno == 0):
			break

	return binary[::-1]


class NumberException(Exception): pass


if __name__ == '__main__':
	
	sOptions = "\nWhat do you want do?"
	sOptions += "\n   1.- Convert octal to decimal number"
	sOptions += "\n   2.- Convert decimal to ocatal number"
	sOptions += "\n   3.- Convert octal to hexadecimal number"
	sOptions += "\n   4.- Convert hexadecimal to octal number"
	sOptions += "\n   0.- Exit\n"

	while 1:
		try:
			option = int(input(sOptions))
		except:
			option = -1

		if option == 1:
			try:
				param = input("Tell me a number to convert: ")
				num_decimal = octal_to_decimal(param)
				print(param + " in the decimal system is: " + str(num_decimal))
			except NumberException: 
				print("The number entered is not valid, try again")
			except:
				print("Invalid param, try again")

		elif (option == 2):
			try:
				param = input("Tell me a number to convert: ")
				num_octal = decimal_to_octal(int(param))
				print(param + " in the octal system is: " + str(num_octal))
			except:
				print("Invalid param, try again")

		elif (option == 3):
			pass
		elif (option == 4):
			pass
		elif (option == 0):
			break
		else:
			print("Invalid option, try again")

	print("See you!")
