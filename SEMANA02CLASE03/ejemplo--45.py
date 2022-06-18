"""Solicitar al usuario un número entero y luego un dígito. Informar la
cantidad de ocurrencias del dígito en el número(en ultimo lugar del numero), utilizando para ello
una función que calcule la frecuencia"""

def frecuencia(numero, digito):
    cantidad =  0
    while numero!=0:
        ultimodigito = numero%10
        if  ultimodigito==digito:
            cantidad = cantidad + 1
        numero = int(numero/10)
    return cantidad

num = int(input("ingresar un numero: "))
udigito = int(input("ingrese digito a encontrar: "))
print("frecuencia del digito {} en el numero {} es de: {} " .format(udigito, num, frecuencia(num, udigito)))



