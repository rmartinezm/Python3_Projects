'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica02/first_program.py

	Escribe funciones que permitan convertir numeros:
		* De decimal a octal y de octal a decimal
	 	* De octal a hexadecimal y hexadecimal a octal
'''

'''
	Convierte un numero del sistema octal al sistema decimal
	@param num_octal
		Numero del sistema octal que convertiremos a numero del sistema decimal
	@raise NumberException
		Si num_octal no es un numero del sistema octal
	@return
		La representacion de num_octal en el sistema decimal
'''
def octal_to_decimal(num_octal):
	n = 0
	num_decimal = 0

	sOctal = str(num_octal)[::-1]

	for number in sOctal:
		if (int(number) > 7):
			raise NumberException()

		num_decimal += int(number) * (8 ** n)
		n += 1

	return num_decimal


'''
	Convierte un numero del sistema decimal al sistema octal
	@param num_decimal
		Numero del sistema decimal que convertiremos a numero del sistema octal
	@return
		La representacion de num_decimal en el sistema octal	
'''
def decimal_to_octal(num_decimal):
	binary = decimal_to_binary(num_decimal)
	octal_number = binary_to_octal(binary)

	return octal_number


'''
	Convierte un numero del sistema octal al sistema hexadecimal
	@param num_octal
		Numero del sistema octal que convertiremos a numero del sistema hexadecimal
	@return
		La representacion de num_octal en el sistema hexadecimal	
'''
def octal_to_hexadecimal(num_octal):
	num_binary  = decimal_to_binary(octal_to_decimal(num_octal))[::-1]
	num_hexadecimal = ""

	aList = ["A", "B", "C", "D", "E", "F"]
	aux_list = []

	for number in num_binary:
		if (len(aux_list) == 4):
			hexadecimal = int(aux_list[0]) * 8
			hexadecimal += int(aux_list[1]) * 4
			hexadecimal += int(aux_list[2]) * 2
			hexadecimal += int(aux_list[3]) * 1
			if (hexadecimal < 10):
				num_hexadecimal = str(hexadecimal) + num_hexadecimal
			else:
				num_hexadecimal = aList[hexadecimal-10] + num_hexadecimal
			aux_list = [number]
		else:
			aux_list.insert(0, number)

	if(aux_list != []):
		while len(aux_list) != 4:
			aux_list.insert(0, "0")
		hexadecimal = int(aux_list[0]) * 8
		hexadecimal += int(aux_list[1]) * 4
		hexadecimal += int(aux_list[2]) * 2
		hexadecimal += int(aux_list[3]) * 1
		if (hexadecimal < 10):
			num_hexadecimal = str(hexadecimal) + num_hexadecimal
		else:
			num_hexadecimal = aList[hexadecimal-10] + num_hexadecimal
	return num_hexadecimal


'''
	Convierte un numero del sistema hexadecimal al sistema octal
	@param num_hexadecimal
		Numero del sistema hexadecimal que convertiremos a numero del sistema octal
	@return
		La representacion de num_hexadecimal en el sistema octal	
'''
def hexadecimal_to_octal(num_hexadecimal):
	num_binary = hexadecimal_to_binary(num_hexadecimal)

	num_octal = binary_to_octal(num_binary)

	return num_octal


'''
	Convierte un numero del sistema decimal al sistema binario
	@param num_decimal
		Numero del sistema decimal que convertiremos a numero del sistema binario
	@return
		La representacion de num_decimal en el sistema binario
'''
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


'''
	Convierte un numero del sistema hexadecimal al sistema binario
	@param num_hexadecimal
		Numero del sistema hexadecimal que convertiremos a numero del sistema binario
	@return
		La representacion de num_hexadecimal en el sistema binario
'''
def hexadecimal_to_binary(num_hexadecimal):
	binary = ""
	aDictionary = {"A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

	aux = num_hexadecimal.upper()

	for num in aux:
		if (num in aDictionary.keys()):
			binary += aDictionary.get(num)
		else:
			a_binary = decimal_to_binary(int(num))
			while len(a_binary) != 4:
				a_binary = "0" + a_binary
			binary += a_binary

	return binary


'''
	Convierte un numero del sistema binario al sistema octal
	@param num_binary
		Numero del sistema binario que convertiremos a numero del sistema octal
	@return
		La representacion de num_binary en el sistema octal
'''
def binary_to_octal(num_binary):
	r_binary = num_binary[::-1]

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

	return int(octal_number)


'''
	Excepcion que se utiliza para identificar los numeros que no corresponden al sistema
	deseado
'''
class NumberException(Exception): pass


if __name__ == '__main__':
	
	sOptions = "\nWhat do you want do?"
	sOptions += "\n   1.- Convert octal to decimal number"
	sOptions += "\n   2.- Convert decimal to octal number"
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
			try:
				param = input("Tell me a number to convert: ")
				num_hexadecimal = octal_to_hexadecimal(int(param))
				print(param + " in the hexadecimal system is: " + num_hexadecimal)
			except:
				print("Invalid param, try again")

		elif (option == 4):
			try:
				param = input("Tell me a number to convert: ")
				num_octal = hexadecimal_to_octal(param)
				print(param + " in the octal system is: " + str(num_octal))
			except:
				print("Invalid param, try again")

		elif (option == 0):
			break
		else:
			print("Invalid option, try again")

	print("See you!")
