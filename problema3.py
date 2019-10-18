"""
	Jdesparza
"""
# se crea un mensaje
mensaje = "No hay medicina que cure lo que no cura la felicidad"
# split convierte una cadena de texto en lista
resultado1 = mensaje.split()
# variable que opera con filter y lambda para encontrar los pronombres
resultado = filter(lambda x: len(x)==2 or len(x)==3, resultado1)
# imprime el resultado
print(list(resultado))