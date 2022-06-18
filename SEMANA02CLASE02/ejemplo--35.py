"manejo de cadenas"

cadena = "conexion a base de datos con python"

cadena2 = cadena.replace(cadena[0:6], "ccc")

print("cadena con reemplazo: ", cadena2)

"eliminando espacion en blanco de mi cadena antes"
cadena3 = "         conexion a base de datos con python"

cadena4 = cadena3.lstrip()

print(cadena4)

"eliminando espacion en blanco de mi cadena despues"
cadena5 = "conexion a base de datos con python     "

cadena6 = cadena5.rstrip()

print(cadena6)





