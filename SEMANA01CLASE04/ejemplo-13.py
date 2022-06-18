"ejercicio"
"crear una lista con 10 valores aleatorios"
"ordenar los elementos de menor a mayor"
import random
milista = []
for indice in range(1, 11):
    milista.append(random.randint(1, 30))

"ordenamiento de la lista"
milista.sort()
for numero in milista:
    print(numero, " ", end="")
