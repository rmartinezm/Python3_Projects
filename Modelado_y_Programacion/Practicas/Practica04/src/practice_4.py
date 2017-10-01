"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practicas/Practica04/src/practice_4.py

	Artimética de primaria
	A los niños les enseñan a sumar números de varias cifras de derecha a izquierda, sumando una cifra cada
	vez. Muchos de ellos encuentran que la operación de “arrastre”(llevo 1), en la que se debe llevar un 1 de
	una posición a la siguiente, es todo un desafı́o. La tarea consiste en contar el número de operaciones de
	arrastre que se producirán en cada conjunto de problemas de suma.
	
	Entrada
	Cada lı́nea de la entrada consta de dos enteros positivos, de menos de 10 cifras. La última lı́nea de la
	entrada es 0 0

	Ejemplo de entrada
	123 456
	555 555
	123 594
	00

	Salida
	Por cada lı́nea de la entrada, excepto la última, se debe calcular la cantidad de operaciones de arrastre
	que se producirán al sumar los dos números, y se mostrará de la forma que vemos en el ejemplo de salida.

	Ejemplo de salida
	No carry operation.
	3 carry operations.
	1 carry operation.

"""

"""
	Regresa una linea con el número de operaciones de arrastre que se producen al sumar los parametros
		Primer número entero que sumaremos
	@param number_two
		Segundo número entero que sumaremos
	@return 
		Una cadena con el número de operaciones de arrastre que se producen de sumar number_one y number_two
"""
def printCarryOperations(number_one, number_two):
	number_a = str(number_one)
	number_b = str(number_two)

	carryOperations = 0

	# Hacemos que ambos tengan la misma longitud
	while (len(number_a) > len(number_b)):
		number_b = "0" + number_b
	while (len(number_b) > len(number_a)):
		number_a = "0" + number_a

	number_length = len(number_a)
	i = 1

	while 1:
		if (i > number_length):
			break
		aux_a = int(number_a[(-i):])
		aux_b = int(number_b[(-i):])
		equal = aux_a + aux_b

		base_10 = "1" + ("0" * i)
		if (equal >= int(base_10)):
			carryOperations += 1
		i += 1

	# Creamos la cadena dependiendo de la cantidad de operaciones de arrastre encontradas
	sCarriyOperations = "No" if carryOperations == 0 else str(carryOperations)
	sCarriyOperations += " carry " + ("operations." if carryOperations > 1 else "operation.") 
	return sCarriyOperations

"""
	Escribe en el archivo que recibe como parametro una línea con el formato deseado si la línea que se
	recibe como parametro es válida, escribe 'Invalid param' si no lo es
	@param output_file
		Archivo en el que se escribe la línea con el formato
	@param line
		Línea que se verifica sea correcta para poder trabajar con ella y escribir en el output_file
"""
def writeALine(output_file, line):
	numbers = line.split(" ")
	to_write = ""
	if (len(numbers) != 2):
		to_write = "Invalid param\n"
	else:
		number_one = -1
		number_two = -1
		try:
			number_one = int(numbers[0])
			number_two = int(numbers[1]) 

			# Evitamos la entrada de números negativos
			if (number_one < 0 or number_two < 0):
				raise Exception()
		except:
			number_one = -1
				
		if (number_one == -1):
			to_write = "Invalid param\n"
		else:
			to_write = printCarryOperations(number_one, number_two) + "\n"

	output_file.write(to_write)


if __name__ == '__main__':
	option = 0
	# Verificamos que la opción sea correcta, sino termanamos el programa
	try:
		option = input("\n¿Cómo quieres introducir la entrada?\n    1.- Terminal\n    2.- Archivo .txt\n")
		option = int(option)
		if (option < 1 or option > 2):
			raise Exception()
	except:
		print("Opción incorrecta. Adios!")
		exit()

	# Verificamos cual es la opción elegida
	if (option == 1):
		
		output_file = open("salida.txt", "w")

		print("Introduce todas las parejas de enteros que desees, cuando termines coloca un par de ceros así: 0 0")
		while 1:
			line = input()
			if (str(line).strip() == "0 0"):
				break
			writeALine(output_file, line)

		print("Se ha creado el archivo salida.txt con la salida de éstos parametros")
		output_file.close()
	else:
		file_name = input("\nDime el nombre de tu archivo (Ejemplo: entradaR1.txt)\n")
		input_file = None
		# Si el archivo de lectua no existe terminamos el programa
		try:
			input_file = open(file_name, "r")
		except:
			print("El archivo no existe. Adios!")
			exit()
		# Creamos un archivo con la salida que tendra el archivo de entrada
		output_file = open("salida_" + file_name, "w")

		# Verificamos cada línea del archivo para ver si es válida
		for line in input_file:
			if (str(line).strip() == "0 0"):
				break
			writeALine(output_file, line)
		print("Se ha creado el archivo salida_" + file_name +" con la salida del archivo " + file_name)

		input_file.close()
		output_file.close()

	print("El programa finalizó correctamente, hasta pronto!")
			


