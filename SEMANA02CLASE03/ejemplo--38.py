"manejo de caracteres"
"encontrar el indice inicial de una cadena dentro de una cadena mayor"

nombre = input("ingrese su nombre: ")
mensaje = "bienvenido {}" .format(nombre)
indice = mensaje.find(nombre)

print("el indice que empieza nuestra sub cadena en la cadena mayor es: ", indice)

mensaje2 = "{}{}{}" .format(mensaje[0:indice], ": ", nombre)
print("{}" .format(mensaje2))
