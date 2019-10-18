"""
	Jdesparza
"""
# se crea una funcion
def es_black_edades(x):
	# se crea una lista con las black_edades
	black_edades = [10, 14, 30, 32, 40, 16]
	# para detreminar los datos que no esten en la lista de black_edades
	if x in black_edades:
		# retorna falso en el caso de que no sea
		return False
	else:
		# retorna verdadero en el caso de que si sea
		return True
# se crea una lista
edad = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
# variable que opera haciendo uso de filter y la funcion
resultado = filter(es_black_edades, edad)
# se imprime los resultados
print(resultado)
print(list(resultado))