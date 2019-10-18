"""
	Jdesparza
"""
# se crea una lista con duplas
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
# se suma haciendo el uso de lambda las posiciones de la dupla para cada apartado
suma = lambda x: x[0]+x[1]+x[2]
# se imprime el resultado en forma de lista
print(list(map(suma, notas)))