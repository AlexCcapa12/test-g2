"manejo de archivos"

"w: abrir el archivo para poder escribir sobre el"
file = open("my_files/file.txt", "w")
file.write("lenguaje multiplataforma: python\n")
file.write("esta basado en poo\n")
file.write("basado en diferentes paradigmas")

file = open("my_files/file.txt", "r")
print("nuestro file tiene el siguiente contenido: ", file.read())

file.close()

