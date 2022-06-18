"""Manejo de excepciones"""

"""Manejo del type para saber que tipo de error ha ocurrido: 'type( )'"""

try:
    val1 = 2 + "mundo"
except Exception as ex:
    print("Ha ocurrido una excepción: ", type(ex))
