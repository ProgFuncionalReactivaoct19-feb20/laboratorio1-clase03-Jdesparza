"""
	Jdesparza
"""
# se crea una funcion
def es_cualitativa(x):
	# se crea una lista con las notas cualitativas a buscar
	cualitativa = ["Regular", "Bueno"]
	# para detreminar que datos tienen una nota cualitativa
	if x[3] in cualitativa:
		# retorna verdadero en el caso de que si sea
		return True
	else:
		# retorna falso en el caso de que no sea
		return False
# se crea una lista con duplas
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
# variable que opera con filter y a travez de la funcion realizada
resultado = filter(es_cualitativa, notas)
# se imprime los resultados
print(resultado)
print(list(resultado))