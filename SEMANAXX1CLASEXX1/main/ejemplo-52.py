"manejo de archivos"
"apertura y lectura de archivos"

"r: abre el archivo en modo de lectura"
file = open("../my_files/file.txt", "r")
print("contenido de nuestro archivo: ", file.read())

#siempre tenemos que cerrar el archivo que hemos abierto al inicio
file.close()
