"""Escribir un programa para gestionar una agenda telefónica con los nombres
y los teléfonos de los clientes de una empresa."""

nombres = ["\nalex, ", "juan, ", "luis, ", "jorge"]
telefonos = ["\n2569856, ", "2563987, ", "25665855, ", "2558514"]

file = open("my_files/crc.txt", "a+")
file.writelines(nombres)
file.writelines(telefonos)


file = open("my_files/agenda.txt", "r")
print("nuestra agenda tiene el siguiente contenido:\n ", file.read())

file.close()
