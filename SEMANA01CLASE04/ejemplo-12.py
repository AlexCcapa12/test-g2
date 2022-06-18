"ejercicio"
"crear un programa que contenga 20 numeros aleatorios"
"mostrar en pantalla su cuadrado y su cubo"

import random
listanumeros = []

for indice in range(1, 21):
    listanumeros.append(random.randint(1, 20))

print(listanumeros)
"contar los valores de la lista"
print(len(listanumeros))

"segundo recorrido"
for numero in listanumeros:
    print("numero", numero, "cuadrado", numero**2, "cubo", numero**3)