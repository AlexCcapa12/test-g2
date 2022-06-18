"""Pedir números al usuario hasta que ingrese el cero. Por cada uno,
mostrar la suma de sus dígitos (utilizando una función que realice dicha
suma)."""

def sumardigitos(numero):
    suma = 0
    while numero !=0:
        digito = numero%10
        suma = suma + digito
        numero = int(numero/10)
    return suma

num = int(input("ingrese un numero a procesar: "))
while num !=0:
    print("suma: ", sumardigitos(num))
    num = int(input("ingrese un numero a procesar: "))

