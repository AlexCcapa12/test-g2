
diccionario = {"nombre", "apellidos", "edad", "dni"}
print(diccionario)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su dni: "))

"convirtiendo el diccionario a una lista"
print(list(diccionario))
print(type(diccionario))

"agregando un nuevo key a nuestro diccionario"
diccionario1 = {"nombre": nombre , "apellidos": apellido , "edad": edad , "dni": dni }
diccionario1["carrera"] = "ingenieria"
print("Nuevo diccionario: ", diccionario1)

"eliminando el key nombre"
del diccionario1["nombre"]
print("Mi diccionario final es: ", diccionario1)





