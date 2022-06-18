"manejo de archivos"

tecnologiabackend = ["\npython, ", "java, ", "ruby, ", "nodejs"]
tecnologiafrontend = ["\nangular, ", "javascript, ", "reactjs, ", "boostrap"]

"apertura de nuestro archivo"
"a+: permite escribir varias lineas de codigo al abrir nuestro archivo"
"a+: escribe nuesvas lineas de textp sin borrar las lineas que ya estaban escritas"
file = open("my_files/file2.txt", "a+")

"writelines: permkite escribir los datos de una lista"
file.writelines(tecnologiabackend)
file.writelines(tecnologiafrontend)

file = open("my_files/file2.txt", "r")
print("el contenido de nuestrp file es: ", file.read())

file.close()


