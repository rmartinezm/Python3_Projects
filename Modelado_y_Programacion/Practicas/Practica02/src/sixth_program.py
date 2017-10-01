'''
	@author 
		Roberto Martínez Medina
	@github 
		https://github.com/rmartinezm/Python3_Projects/blob/master/Modelado_y_Programacion/Practicas/Practica02/src/sixth_program.py


	Escribe una función que se llame gusanito que reciba un entero k e imprima
	en pantalla una figura compuesta con k asteriscos y entre cada asterisco
	k-n ceros, donde n va de 1 a k-1, al inicio deberás poner un @
	Ejemplo: gusanito(5) imprimirı́a:
	@*0000*000*00*0*
'''

from random import randrange

'''
	Regresa una figura compuesta con k asteriscos y entre cada asterisco k-n ceros,
	donde n vaa de 1 a k-1
	@param k
		Entero con el dibujaremos el gusanito
'''
def gusanito(k):
	gusanito = "@"
	k -= 1
	while k > 0:
		gusanito += "*" + ("0" * k)
		k -= 1
	return gusanito

if __name__ == '__main__':
	rand = randrange(15)
	print("Número k = " + str(rand))
	print(gusanito(rand))
