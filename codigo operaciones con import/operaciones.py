def Suma(numero1,numero2):
	resultado = numero1 + numero2
	return resultado
def Resta(numero1,numero2):
	resultado = numero1 - numero2
	return resultado
def Multiplicacion(numero1,numero2):
	resultado = numero1 * numero2
	return resultado
def Division(numero1,numero2):
	if (numero2 == 0):
		print("El segundo numero no puede ser cero para realizar la division")
		return "No calculado"
	else:
		resultado = numero1 / numero2
		return resultado
