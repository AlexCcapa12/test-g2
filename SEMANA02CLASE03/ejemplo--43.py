"""Pedir números al usuario hasta que ingrese el cero. Por cada uno,
mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de
todos los números ingresados y la suma de sus dígitos. Reutilizar la
misma función realizada en el ejercicio 2."""

def sumardigitos(numero):
    suma = 0
    while numero !=0:
        digito = numero%10
        suma = suma + digito
        numero = int(numero/10)
    return suma

sumatoria = 0
num = int(input("ingrese un numero a procesar: "))
while num !=0:
    print("la suma es: ", sumardigitos(num))
    sumatoria = sumatoria + num
    num = int(input("ingrese un numero a procesar: "))

print("sumatoria final es: ", sumatoria)
print("suma de  digitos: ", sumardigitos(sumatoria))



