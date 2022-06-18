"problema propuesto"
diccionario = {"curso1": "mate", "curso2": "calculo", "curso3": "fisica",
               "curso4": "economia", "curso5": "lenguaje", "curso6": "evolucion"}
print(diccionario)

del diccionario["curso3"]
print("Mi diccionario final es: ", diccionario)

milista = list(diccionario.values())
varcomprobacion = "lenguaje" in milista
print("valor de comprobacion de dato en mi lista: ", varcomprobacion)

diccionario["carrera"] = "ingenieria"
print("Nuevo diccionario: ", diccionario)

list(diccionario)
print("Mi diccionario convertido es el siguiente: ", list(diccionario))
