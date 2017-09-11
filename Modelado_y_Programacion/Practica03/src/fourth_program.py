"""
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practica03/fourth_program.py

	Crea un archivo de excel con las siguientes columnas:
	
	Nombre del empleado
	Apellido paterno
	Apellido materno
	Enero
	Febrero
	Marzo
	...
	Diciembre

	Este archivo deberá tener 20 renglones, es decir, el registro de 20 trabajadores.
	Cada valor en las columnas de los meses deberá tener una cantidad de tipo flotante.
	La actividad consistirá en que realices la lectura de cada celda de todos los meses para cada tra-
	bajador y calcules el monto de un bono a pagarse que deberá ser equivalente al 15 % del total que
	haya percibido a lo largo del año, (puede haber columnas que tengan la cantidad 0.00 eso significa
	que ese mes el trabajador no percibió ingresos)
	Tu programa deberá escribir en un archivo extras.txt el nombre y apellidos de cada trabajador junto
	con la cantidad de dinero adicional que recibirá.
"""

import xlrd

if __name__ == '__main__':
	
	workbook = xlrd.open_workbook("archivo.xlsx")
	archivo = open("extras.txt", "w")

	worksheet = workbook.sheet_by_index(0)

	# Nombres de los empleados		Apellidos paternos		Apellidos Maternos
	# cell(0,1) -> cell(0,20) 		cell(1,1) -> cell(1,20) cell(2,1) -> cell(2,20)

	i_columna = 0
	j_fila = 0
	aString = ""

	# Para cada Fila 
	for j in range(20):
		i_columna = 0
		j_fila = j+1

		aString = ""
		aList = []

		# Para cada columna
		for i in range(15):
			# Los nombres
			if (i < 3):
				aString += worksheet.cell(j_fila, i_columna).value + " "
				i_columna += 1
			# Las cantidades
			else:
				aList.append(worksheet.cell(j_fila, i_columna).value)
				i_columna += 1

		dinero_total = 0
		for mes in aList:
			dinero_total += mes

		bono = (dinero_total/12.0) * .15
		aString += "{0:.2f}\n".format(bono)
		archivo.write(aString)

	archivo.close()