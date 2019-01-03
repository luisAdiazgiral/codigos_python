from operaciones import *
print("Bienvenido al programa de operaciones \n")
def Menu():
	print("seleccione una operacion para proceder :\n")
	print("1.- Suma")
	print("2.- Resta")
	print("3.- Multiplicacion")
	print("4.- Division")
def Opci():
	selec = int(input("ingrese su selección: \n "))
	if (selec == 1):
		Sumar()
	elif (selec == 2):
		Restar()
	elif (selec == 3):
		Multiplicar()
	elif (selec == 4):
		Dividir()
	else:
		print("Elija una opcion del 1 al 4")
def Sumar():
	n1 = int(input("ingrese el primer numero para sumar: "))
	n2 = int(input("ingrese el segundo numero a sumar: "))
	resultado = Suma(n1,n2)
	print("el resultado es: " , resultado)
def Restar():
	n1 = int(input("ingrese el primer numero para restar: "))
	n2 = int(input("ingrese el segundo numero a restar: "))
	resultado = Resta(n1,n2)
	print("el resultado es: " , resultado)
def Multiplicar():
	n1 = int(input("ingrese el primer numero para multiplicar: "))
	n2 = int(input("ingrese el segundo numero a multiplicar: "))
	resultado = Multiplicacion(n1,n2)
	print("el resultado es: " , resultado)
def Dividir():
	n1 = int(input("ingrese el primer numero para dividir: "))
	n2 = int(input("ingrese el segundo numero a dividir: "))
	resultado = Division(n1,n2)
	print("el resultado es: " , resultado)

	#return selec
Menu()
#opc=seleccion
Opci()
#print("el resultado es: " , resultado)
