"""lista con 10 valores aleatorios"""

import random

lista1 = []

for indice in range(1, 11):
    lista1.append(random.randint(1, 10))
for numero in lista1:
    print(numero, " ", end="")

for numero in lista1:
    #print()
    print(numero**2, " ", end="")
#for numero in lista1:
 #   print("\nlos cuadrados son: ", numero**2, " ")

for numero in lista1:
    print("\nlos cubos son: ", numero**3, " ")



