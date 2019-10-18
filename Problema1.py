"""
	Jdesparza
"""
datos = open("promedios.txt", "r")
resultado1 = datos.split()
resultado2 = []
for i in resultado1:
	resultado2.append(i)

print(list(resultado2))