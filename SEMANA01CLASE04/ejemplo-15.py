"ejercicio"
"crea tu primer diccionario con los campos de tecnologia y tipo"
midiccionario = {"nombre": "amazon web", "tipo": "cloud"}

"convirtiendo el diccionario a una lista"
print(list(midiccionario))

"agregando un nuevo key a nuestro diccionario"
midiccionario["antiguedad"] = 16
print(midiccionario)

"verificar valor en diccionario"
milista = list(midiccionario.values())
varcomprobacion = "amazon web" in milista
print("valor de comprobacion de dato en mi lista: ", varcomprobacion)

"crear un diccionario con los mismos valores sin apuntar a una variable osea con el dict"
print(dict([("herramientas", "scrum")]))



