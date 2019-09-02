from operator import itemgetter

def mas_repetido(matriz):
	counter = 0
	num = matriz[0] 
      
	for i in matriz: 
		curr_frequency = matriz.count(i) 
		if(curr_frequency > counter): 
			counter = curr_frequency 
			num = i 
  
	return num 

def condensa(cadena):
	x = {x:cadena.count(x) for x in cadena}
	return sorted(x.iteritems(), key=itemgetter(1))

def triangulo_pascal(niveles):
    if niveles == 0:
        return []
    elif niveles == 1:
        return [1]
    else:
		triangulo = []
		fila = []
		fila_anterior = triangulo_pascal(niveles-1)
		for i in xrange(0, niveles + 1):
			fila = [j > 0 and j < i - 1 and i > 2 and fila_anterior[j-1] + fila_anterior[j] or 1 for j in xrange(0, i)]
			fila_anterior = fila
			triangulo += [fila]
		return triangulo[1:]

#no pude ordenar las subcadenas por tamanio
def subcadenas(cadena):
	lst = [cadena]
	if len(cadena) > 0:
		lst.extend(subcadenas(cadena[1:]))
		lst.extend(subcadenas(cadena[:-1]))
	return sorted(list(set(lst)))


if __name__ == '__main__':
	opcion = raw_input("Bienvenido. Que quieres hacer?" + "\n" +
		"1. Elemento mas repetido de una matriz 2x2." + "\n" +
		"2. Condensar una cadena."  + "\n" +
		"3. Triangulo de Pascal." + "\n" +
		"4. Subcadenas."  + "\n")
	try:
		num_opcion=int(opcion)
		if num_opcion == 1:
			try:
				x00 = raw_input("Ingresa el valor 00" + "\n")
				x01 = raw_input("Ingresa el valor 01" + "\n")
				x10 = raw_input("Ingresa el valor 10" + "\n")
				x11 = raw_input("Ingresa el valor 11" + "\n")
				matriz = [int(x00), int(x01), int(x10), int(x11)]
				resultado = mas_repetido(matriz)
				print("El valor mas repetido es: " + str(resultado))
			except ValueError:
				print("Las matrices solo aceptan numeros")

		elif num_opcion == 2:
			cadena = raw_input("Ingresa la cadena a condensar." + "\n")
			resultado = condensa(cadena)
			print("La cadena condensada es: " + "\n")
			print(resultado)

		elif num_opcion == 3:
			try:
				niveles = raw_input("Ingresa el numero de niveles para el triangulo de Pascal: " + "\n")
				triangulo = triangulo_pascal(int(niveles))
				print("El triangulo es: " + "\n")
				print(triangulo)
			except ValueError:
				print("Debes ingresar un numero")

		elif num_opcion == 4:
			cadena = raw_input("Ingresa la cadena a dividir." + "\n")
			resultado = subcadenas(cadena)
			print("Lo siento, no puedo ordenar las subcadenas, pero puedo dividir tu entrada: " + "\n")
			print(resultado)

		else:
			print("Ingresa una opcion valida")
	except ValueError:
		print("Ingresa una opcion valida")

		